# gui.py

import os
import queue
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from config import DEFAULT_PARAMS
from dataclasses import dataclass
from enum import Enum, auto

class UIMessageType(Enum):
    STATUS = auto()
    ANALYSIS_COMPLETE = auto()
    ERROR = auto()

@dataclass
class UIMessage:
    type: UIMessageType
    data: any = None

class BPMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Heartbeat BPM Analyzer")
        self.root.geometry("550x350")
        self.style = ttkb.Style(theme='minty')
        self.current_file = None
        self.params = DEFAULT_PARAMS.copy() # Assumes DEFAULT_PARAMS is imported
        self.log_queue = queue.Queue()
        self.create_widgets()
        self.root.after(100, self.process_log_queue)
        self._find_initial_audio_file()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # File selection
        file_frame = ttk.LabelFrame(main_frame, text="Audio File", padding=10)
        file_frame.pack(fill=tk.X, pady=5)
        self.file_label = ttk.Label(file_frame, text="No file selected", wraplength=450)
        self.file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.select_file, bootstyle=INFO)
        browse_btn.pack(side=tk.RIGHT, padx=5)

        # Parameters
        param_frame = ttk.LabelFrame(main_frame, text="Analysis Parameters", padding=10)
        param_frame.pack(fill=tk.X, pady=5)
        ttk.Label(param_frame, text="Starting BPM (optional):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.bpm_entry = ttk.Entry(param_frame)
        self.bpm_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)

        # Action Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=20)
        self.analyze_btn = ttk.Button(btn_frame, text="Analyze", command=self.start_analysis_thread, bootstyle=SUCCESS, state=tk.DISABLED)
        self.analyze_btn.pack(side=tk.RIGHT, padx=5)

        # Status Bar
        self.status_var = tk.StringVar(value="Select an audio file to begin.")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, padding=5)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))

        param_frame.columnconfigure(1, weight=1)

    def process_log_queue(self):
        try:
            while not self.log_queue.empty():
                msg: UIMessage = self.log_queue.get(0)

                if msg.type == UIMessageType.STATUS:
                    self.status_var.set(msg.data)
                elif msg.type == UIMessageType.ANALYSIS_COMPLETE:
                    self.status_var.set("Analysis complete!")
                    self.analyze_btn.config(state=tk.NORMAL)
                elif msg.type == UIMessageType.ERROR:
                     self.status_var.set("An error occurred. Check logs.")
                     self.analyze_btn.config(state=tk.NORMAL)
                     messagebox.showerror("Analysis Error", msg.data)

        finally:
            self.root.after(100, self.process_log_queue)

    def select_file(self):
        filetypes = [('Audio files', '*.wav *.mp3 *.m4a *.flac *.ogg *.mp4 *.mkv *.mov'), ('All files', '*.*')]
        filename = filedialog.askopenfilename(title="Select audio file", filetypes=filetypes)
        if filename:
            self.current_file = filename
            self.file_label.config(text=os.path.basename(filename))
            self.analyze_btn.config(state=tk.NORMAL)
            self._update_status(f"Ready to analyze: {os.path.basename(filename)}")

    def _find_initial_audio_file(self):
        supported = ('.wav', '.mp3', '.m4a', '.flac', '.ogg', '.mp4', '.mkv', '.mov')
        try:
            for filename in os.listdir(os.getcwd()):
                if filename.lower().endswith(supported):
                    self.current_file = os.path.join(os.getcwd(), filename)
                    self.file_label.config(text=os.path.basename(self.current_file))
                    self.analyze_btn.config(state=tk.NORMAL)
                    self._update_status(f"Auto-loaded: {os.path.basename(self.current_file)}")
                    return
        except Exception as e:
            # Assumes logging is configured in the main script
            # logging.error(f"Could not auto-find file: {e}")
            pass

    def _update_status(self, message):
        """Safely update the status bar from any thread."""
        self.root.after(0, lambda: self.status_var.set(message))

    def start_analysis_thread(self):
        """Starts the analysis in a new thread."""
        if not self.current_file:
            messagebox.showerror("Error", "No file selected")
            return

        self.analyze_btn.config(state=tk.DISABLED)
        self._update_status("Starting analysis...")

        analysis_thread = threading.Thread(target=self._run_analysis_in_background)
        analysis_thread.daemon = True
        analysis_thread.start()

    def _run_analysis_in_background(self):
        try:
            from bpm_analysis import analyze_wav_file, convert_to_wav

            bpm_input = self.bpm_entry.get().strip()
            start_bpm_hint = float(bpm_input) if bpm_input else None

            converted_dir = os.path.join(os.getcwd(), "converted_wavs")
            os.makedirs(converted_dir, exist_ok=True)
            base_name, ext = os.path.splitext(self.current_file)
            wav_path = os.path.join(converted_dir, f"{os.path.basename(base_name)}.wav")

            if ext.lower() != '.wav':
                self.log_queue.put(UIMessage(UIMessageType.STATUS, "Converting file to WAV..."))
                if not convert_to_wav(self.current_file, wav_path):
                    self.log_queue.put(UIMessage(UIMessageType.ERROR, "File conversion failed."))
                    return
            else:
                import shutil
                shutil.copy(self.current_file, wav_path)

            self.log_queue.put(UIMessage(UIMessageType.STATUS, "Processing and analyzing heartbeat..."))
            # Assumes analyze_wav_file is imported
            analyze_wav_file(wav_path, self.params, start_bpm_hint)
            self.log_queue.put(UIMessage(UIMessageType.ANALYSIS_COMPLETE))

        except Exception as e:
            error_info = f"An error occurred:\n{str(e)}"
            self.log_queue.put(UIMessage(UIMessageType.ERROR, error_info))
