# gui.py

import os
import queue
import threading
import tkinter as tk
import json
import subprocess
import platform
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
        self.root.title("Heartbeat BPM Analyzer (Batch Mode)")
        self.root.geometry("800x600")
        self.style = ttkb.Style(theme='minty')
        self.current_files = []
        self.params = DEFAULT_PARAMS.copy()
        self.log_queue = queue.Queue()
        self.settings_file = os.path.join(os.getcwd(), "ui_settings.json")
        self._loading_settings = True  # Prevent saving during initialization
        self.create_widgets()
        self.load_ui_settings()
        self._loading_settings = False  # Re-enable saving after load
        self.root.after(100, self.process_log_queue)
        self._find_initial_audio_file()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # File selection
        file_frame = ttk.LabelFrame(main_frame, text="Audio File(s)", padding=10)
        file_frame.grid(row=0, column=0, sticky="ew", pady=5)
        self.file_label = ttk.Label(file_frame, text="No files selected", wraplength=450)
        self.file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.select_file, bootstyle=INFO)
        browse_btn.pack(side=tk.RIGHT, padx=5)

        # Parameters
        param_frame = ttk.LabelFrame(main_frame, text="Analysis Parameters", padding=10)
        param_frame.grid(row=1, column=0, sticky="ew", pady=5)
        ttk.Label(param_frame, text="Starting BPM (optional):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.bpm_entry = ttk.Entry(param_frame)
        self.bpm_entry.grid(row=0, column=1, sticky=tk.EW, padx=5, pady=2)
        # Save settings when BPM entry changes
        self.bpm_entry.bind('<KeyRelease>', lambda e: self.save_ui_settings())
        self.bpm_entry.bind('<FocusOut>', lambda e: self.save_ui_settings())

        # Output file options
        self.output_html = tk.BooleanVar(value=True)
        self.output_csv = tk.BooleanVar(value=False)
        self.output_summary = tk.BooleanVar(value=False)
        self.output_debug = tk.BooleanVar(value=False)
        self.output_settings = tk.BooleanVar(value=False)
        self.output_filtered_wav = tk.BooleanVar(value=False)
        self.output_bpm_text = tk.BooleanVar(value=False)
        # HTML spectrogram overlay can be slow to generate; expose as a separate toggle.
        self.output_spectrogram = tk.BooleanVar(value=True)

        # Output files section
        output_frame = ttk.LabelFrame(main_frame, text="Output Files", padding="10")
        output_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

        # Output file checkboxes
        ttk.Checkbutton(output_frame, text="HTML Report", variable=self.output_html, 
                       command=self._update_output_status).grid(row=0, column=0, sticky="w", padx=(0, 20))
        ttk.Checkbutton(output_frame, text="CSV Data", variable=self.output_csv, 
                       command=self._update_output_status).grid(row=0, column=1, sticky="w", padx=(0, 20))
        ttk.Checkbutton(output_frame, text="Summary Report", variable=self.output_summary, 
                       command=self._update_output_status).grid(row=1, column=0, sticky="w", padx=(0, 20))
        ttk.Checkbutton(output_frame, text="Debug Report", variable=self.output_debug, 
                       command=self._update_output_status).grid(row=1, column=1, sticky="w", padx=(0, 20))
        ttk.Checkbutton(output_frame, text="Analysis Settings", variable=self.output_settings, 
                       command=self._update_output_status).grid(row=2, column=0, sticky="w", padx=(0, 20))
        ttk.Checkbutton(output_frame, text="Filtered Audio WAV", variable=self.output_filtered_wav, 
                       command=self._update_output_status).grid(row=2, column=1, sticky="w", padx=(0, 20))
        ttk.Checkbutton(output_frame, text="BPM Time Text", variable=self.output_bpm_text,
                       command=self._update_output_status).grid(row=3, column=0, sticky="w", padx=(0, 20))
        ttk.Checkbutton(output_frame, text="HTML Spectrogram", variable=self.output_spectrogram,
                       command=self._update_output_status).grid(row=3, column=1, sticky="w", padx=(0, 20))

        # Select All/None buttons
        btn_frame_output = ttk.Frame(output_frame)
        btn_frame_output.grid(row=4, column=0, columnspan=2, pady=(10, 0))
        ttk.Button(btn_frame_output, text="Select All", command=self.select_all_outputs, 
                  bootstyle=SECONDARY).grid(row=0, column=0, padx=(0, 5))
        ttk.Button(btn_frame_output, text="Select None", command=self.select_none_outputs, 
                  bootstyle=SECONDARY).grid(row=0, column=1)

        # Output status label
        self.output_status_label = ttk.Label(output_frame, text="", font=("TkDefaultFont", 9))
        self.output_status_label.grid(row=5, column=0, columnspan=2, pady=(5, 0))
        
        # Bind output option changes to update status and save settings
        def on_output_change(*args):
            self._update_output_status()
            self.save_ui_settings()
        
        self.output_html.trace('w', on_output_change)
        self.output_csv.trace('w', on_output_change)
        self.output_summary.trace('w', on_output_change)
        self.output_debug.trace('w', on_output_change)
        self.output_settings.trace('w', on_output_change)
        self.output_filtered_wav.trace('w', on_output_change)
        self.output_bpm_text.trace('w', on_output_change)
        self.output_spectrogram.trace('w', on_output_change)

        # Action Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.grid(row=3, column=0, sticky="ew", pady=20)
        self.analyze_btn = ttk.Button(btn_frame, text="Analyze", command=self.start_analysis_thread, bootstyle=SUCCESS, state=tk.DISABLED)
        self.analyze_btn.pack(side=tk.RIGHT, padx=5)
        self.open_html_btn = ttk.Button(btn_frame, text="Open Last HTML Report", command=self.open_last_html, bootstyle=INFO)
        self.open_html_btn.pack(side=tk.RIGHT, padx=5)

        # Status Bar
        self.status_var = tk.StringVar(value="Select one or more audio files to begin.")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W, padding=5)
        status_bar.grid(row=4, column=0, sticky="ew", pady=(10, 0))

        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        param_frame.columnconfigure(1, weight=1)
        output_frame.columnconfigure(0, weight=1)
        output_frame.columnconfigure(1, weight=1)

    def process_log_queue(self):
        try:
            while not self.log_queue.empty():
                msg: UIMessage = self.log_queue.get(0)

                if msg.type == UIMessageType.STATUS:
                    self.status_var.set(msg.data)
                elif msg.type == UIMessageType.ANALYSIS_COMPLETE:
                    final_message = msg.data if msg.data else "Analysis complete!"
                    self.status_var.set(final_message)
                    self.analyze_btn.config(state=tk.NORMAL)
                elif msg.type == UIMessageType.ERROR:
                     self.status_var.set("An error occurred. Check logs and messagebox.")
                     messagebox.showerror("Analysis Error", msg.data)
        finally:
            self.root.after(100, self.process_log_queue)

    def select_file(self):
        filetypes = [('Audio files', '*.wav *.mp3 *.m4a *.flac *.ogg *.mp4 *.mkv *.mov'), ('All files', '*.*')]
        filenames = filedialog.askopenfilename(
            title="Select one or more audio files",
            filetypes=filetypes,
            multiple=True
        )
        if filenames:
            self.current_files = list(filenames)
            label_text = f"{len(self.current_files)} files selected"
            self.file_label.config(text=label_text)
            self.analyze_btn.config(state=tk.NORMAL)
            
            # Save the selected files to settings
            self.save_ui_settings()

            # If only one file is chosen, try to load its settings.
            if len(self.current_files) == 1:
                self._load_settings_for_file(self.current_files[0])
            else:
                # If multiple files are selected, clear the entry to avoid confusion.
                # The user must enter a value to be used for the whole batch.
                self.bpm_entry.delete(0, tk.END)
                self._update_status(f"Ready to analyze {len(self.current_files)} files.")

    def _find_initial_audio_file(self):
        """
        Automatically finds all supported audio files in the current directory
        and loads them into the application. If only one file is found, it
        attempts to load its corresponding analysis settings.
        Only runs if no files were already loaded from saved settings.
        """
        # Skip auto-detection if files were already loaded from saved settings
        if self.current_files:
            return
            
        supported = ('.wav', '.mp3', '.m4a', '.flac', '.ogg', '.mp4', '.mkv', '.mov')
        found_files = []
        try:
            # Find all supported files in the script's directory
            for filename in os.listdir(os.getcwd()):
                if filename.lower().endswith(supported):
                    full_path = os.path.join(os.getcwd(), filename)
                    found_files.append(full_path)

            if found_files:
                self.current_files = found_files

                # Update the GUI to show what was loaded
                label_text = f"{len(self.current_files)} files loaded"
                self.file_label.config(text=label_text)
                self.analyze_btn.config(state=tk.NORMAL)
                
                # Save the auto-detected files to settings
                self.save_ui_settings()

                # If only one file was auto-detected, try to load its settings
                if len(self.current_files) == 1:
                    self._load_settings_for_file(self.current_files[0])
                else:
                    # Otherwise, set a general status for batch processing
                    self._update_status(f"Auto-loaded {len(self.current_files)} files from the current directory.")

        except Exception as e:
            # Fails silently if it can't read the directory
            pass

    def _load_settings_for_file(self, file_path: str):
        """Checks for and loads 'start_bpm_hint' from a corresponding JSON file."""
        output_dir = os.path.join(os.getcwd(), "processed_files")
        base_name, _ = os.path.splitext(os.path.basename(file_path))
        settings_path = os.path.join(output_dir, f"{base_name}_Analysis_Settings.json")

        self.bpm_entry.delete(0, tk.END)

        if os.path.exists(settings_path):
            try:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)

                if settings.get('start_bpm_hint') is not None:
                    bpm_value = settings['start_bpm_hint']
                    self.bpm_entry.insert(0, str(bpm_value))
                    self._update_status(f"Loaded BPM hint ({bpm_value}) from settings file.")
                else:
                    self._update_status(f"Found settings file, but no BPM hint inside.")
            except Exception as e:
                self._update_status(f"Error reading settings file for {os.path.basename(file_path)}.")
                print(f"ERROR: Could not parse {settings_path}. Details: {e}")
        else:
            self._update_status(f"Ready to analyze. No previous settings file found.")

    def _update_status(self, message):
        """Safely update the status bar from any thread."""
        self.root.after(0, lambda: self.status_var.set(message))

    def save_ui_settings(self):
        """Save current UI settings to a JSON file."""
        # Don't save during initialization when loading settings
        if self._loading_settings:
            return
        try:
            settings = {
                'starting_bpm': self.bpm_entry.get().strip(),
                'output_html': self.output_html.get(),
                'output_csv': self.output_csv.get(),
                'output_summary': self.output_summary.get(),
                'output_debug': self.output_debug.get(),
                'output_settings': self.output_settings.get(),
                'output_filtered_wav': self.output_filtered_wav.get(),
                'output_bpm_text': self.output_bpm_text.get(),
                'output_spectrogram': self.output_spectrogram.get(),
                'last_files': self.current_files if self.current_files else []
            }
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4)
        except Exception as e:
            # Silently fail - don't interrupt user workflow
            print(f"Warning: Could not save UI settings: {e}")

    def load_ui_settings(self):
        """Load UI settings from a JSON file if it exists."""
        if not os.path.exists(self.settings_file):
            return
        
        self._loading_settings = True  # Prevent saving during load
        try:
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
            
            # Load starting BPM
            if 'starting_bpm' in settings and settings['starting_bpm']:
                self.bpm_entry.delete(0, tk.END)
                self.bpm_entry.insert(0, settings['starting_bpm'])
            
            # Load output options
            if 'output_html' in settings:
                self.output_html.set(settings['output_html'])
            if 'output_csv' in settings:
                self.output_csv.set(settings['output_csv'])
            if 'output_summary' in settings:
                self.output_summary.set(settings['output_summary'])
            if 'output_debug' in settings:
                self.output_debug.set(settings['output_debug'])
            if 'output_settings' in settings:
                self.output_settings.set(settings['output_settings'])
            if 'output_filtered_wav' in settings:
                self.output_filtered_wav.set(settings['output_filtered_wav'])
            if 'output_bpm_text' in settings:
                self.output_bpm_text.set(settings['output_bpm_text'])
            if 'output_spectrogram' in settings:
                self.output_spectrogram.set(settings['output_spectrogram'])
            
            # Load last used files (only if they still exist)
            if 'last_files' in settings and settings['last_files']:
                existing_files = []
                for file_path in settings['last_files']:
                    if os.path.exists(file_path):
                        existing_files.append(file_path)
                
                if existing_files:
                    self.current_files = existing_files
                    label_text = f"{len(self.current_files)} files loaded from previous session"
                    self.file_label.config(text=label_text)
                    self.analyze_btn.config(state=tk.NORMAL)
                    
                    # If only one file was loaded, try to load its settings
                    if len(self.current_files) == 1:
                        self._load_settings_for_file(self.current_files[0])
                    else:
                        self._update_status(f"Loaded {len(self.current_files)} files from previous session.")
                
        except Exception as e:
            # Silently fail - just use defaults
            print(f"Warning: Could not load UI settings: {e}")
        finally:
            self._loading_settings = False  # Re-enable saving

    def open_last_html(self):
        """Find and open the most recently generated HTML report file."""
        output_dir = os.path.join(os.getcwd(), "processed_files")
        
        if not os.path.exists(output_dir):
            messagebox.showwarning("No Reports", "No processed files directory found. Run an analysis first.")
            return
        
        # Find all HTML files matching the pattern *_bpm_plot.html
        html_files = []
        try:
            for filename in os.listdir(output_dir):
                if filename.endswith("_bpm_plot.html"):
                    file_path = os.path.join(output_dir, filename)
                    # Get modification time
                    mtime = os.path.getmtime(file_path)
                    html_files.append((mtime, file_path, filename))
        except Exception as e:
            messagebox.showerror("Error", f"Could not read processed files directory: {e}")
            return
        
        if not html_files:
            messagebox.showwarning("No Reports", "No HTML reports found. Run an analysis first.")
            return
        
        # Sort by modification time (most recent first)
        html_files.sort(reverse=True)
        most_recent_file = html_files[0][1]
        
        # Open the file with the system's default application
        try:
            if platform.system() == 'Windows':
                os.startfile(most_recent_file)
            elif platform.system() == 'Darwin':  # macOS
                subprocess.run(['open', most_recent_file])
            else:  # Linux and others
                subprocess.run(['xdg-open', most_recent_file])
            self._update_status(f"Opened: {os.path.basename(most_recent_file)}")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Could not open HTML file: {e}")

    def select_all_outputs(self):
        """Select all output file options."""
        self.output_html.set(True)
        self.output_csv.set(True)
        self.output_summary.set(True)
        self.output_debug.set(True)
        self.output_settings.set(True)
        self.output_filtered_wav.set(True)
        self.output_bpm_text.set(True)
        self.output_spectrogram.set(True)

    def select_none_outputs(self):
        """Deselect all output file options."""
        self.output_html.set(False)
        self.output_csv.set(False)
        self.output_summary.set(False)
        self.output_debug.set(False)
        self.output_settings.set(False)
        self.output_filtered_wav.set(False)
        self.output_bpm_text.set(False)
        self.output_spectrogram.set(False)

    def get_output_options(self):
        """Get the current output file selection as a dictionary."""
        return {
            'html': self.output_html.get(),
            'csv': self.output_csv.get(),
            'summary': self.output_summary.get(),
            'debug': self.output_debug.get(),
            'settings': self.output_settings.get(),
            'filtered_wav': self.output_filtered_wav.get(),
            'bpm_text': self.output_bpm_text.get(),
            'spectrogram': self.output_spectrogram.get(),
        }

    def _update_output_status(self, *args):
        """Update the output status label based on current selections."""
        output_options = self.get_output_options()
        selected_count = sum(output_options.values())
        total_count = len(output_options)
        
        if selected_count == 0:
            self.output_status_label.config(text="No output types selected", foreground="red")
        elif selected_count == total_count:
            self.output_status_label.config(text="All output types selected", foreground="green")
        else:
            self.output_status_label.config(text=f"{selected_count}/{total_count} output types selected", foreground="orange")

    def start_analysis_thread(self):
        """Starts the analysis in a new thread."""
        if not self.current_files:
            messagebox.showerror("Error", "No files selected")
            return

        # Check if at least one output option is selected
        output_options = self.get_output_options()
        if not any(output_options.values()):
            messagebox.showerror("Error", "Please select at least one output file type to generate.")
            return

        # Save settings before starting analysis
        self.save_ui_settings()

        self.analyze_btn.config(state=tk.DISABLED)
        self._update_status(f"Starting batch analysis of {len(self.current_files)} files...")

        analysis_thread = threading.Thread(target=self._run_analysis_in_background)
        analysis_thread.daemon = True
        analysis_thread.start()

    def _run_analysis_in_background(self):
        try:
            from bpm_analysis import analyze_wav_file
            from audio_io import convert_to_wav
            import shutil

            # Check for a global BPM value to override all individual settings.
            bpm_override_input = self.bpm_entry.get().strip()
            bpm_override_hint = float(bpm_override_input) if bpm_override_input else None

            output_dir = os.path.join(os.getcwd(), "processed_files")
            os.makedirs(output_dir, exist_ok=True)

            total_files = len(self.current_files)
            files_processed = 0
            errors = []

            # --- BATCH PROCESSING LOOP ---
            for i, file_path in enumerate(self.current_files):
                try:
                    self.log_queue.put(UIMessage(UIMessageType.STATUS,
                                                 f"({i + 1}/{total_files}) Processing: {os.path.basename(file_path)}"))

                    # --- START: Per-File Settings Logic ---
                    # The BPM hint to be used for the current file.
                    start_bpm_hint = None
                    if bpm_override_hint is not None:
                        # Use the global override if the user entered a value.
                        start_bpm_hint = bpm_override_hint
                    else:
                        # Otherwise, try to load settings for this specific file.
                        base_name_for_settings, _ = os.path.splitext(os.path.basename(file_path))
                        settings_path = os.path.join(output_dir, f"{base_name_for_settings}_Analysis_Settings.json")
                        if os.path.exists(settings_path):
                            try:
                                with open(settings_path, 'r', encoding='utf-8') as f:
                                    settings = json.load(f)
                                if settings.get('start_bpm_hint') is not None:
                                    start_bpm_hint = float(settings['start_bpm_hint'])
                            except Exception:
                                # If file is corrupt or unreadable, just proceed without the hint.
                                pass
                    # --- END: Per-File Settings Logic ---

                    base_name, ext = os.path.splitext(file_path)
                    wav_path = os.path.join(output_dir, f"{os.path.basename(base_name)}.wav")

                    if ext.lower() != '.wav':
                        self.log_queue.put(UIMessage(UIMessageType.STATUS,
                                                     f"({i + 1}/{total_files}) Converting {os.path.basename(file_path)}..."))
                        if not convert_to_wav(file_path, wav_path):
                            raise Exception("File conversion failed.")
                    else:
                        shutil.copy(file_path, wav_path)

                    self.log_queue.put(
                        UIMessage(UIMessageType.STATUS, f"({i + 1}/{total_files}) Analyzing heartbeat..."))

                    # Pass the file-specific start_bpm_hint and output options to the analysis function.
                    output_options = self.get_output_options()
                    analyze_wav_file(wav_path, self.params, start_bpm_hint, original_file_path=file_path,
                                     output_directory=output_dir, output_options=output_options)
                    files_processed += 1

                except Exception as e:
                    # Inner try-except block to handle errors for a single file
                    error_info = f"Error processing '{os.path.basename(file_path)}':\n{str(e)}"
                    self.log_queue.put(UIMessage(UIMessageType.ERROR, error_info))
                    errors.append(os.path.basename(file_path))

            # --- POST-LOOP COMPLETION MESSAGE ---
            if not errors:
                completion_message = f"Successfully processed all {total_files} files."
            else:
                completion_message = f"Batch finished. Processed {files_processed}/{total_files}. Errors in: {', '.join(errors)}"

            self.log_queue.put(UIMessage(UIMessageType.ANALYSIS_COMPLETE, completion_message))

        except Exception as e:
            # Outer try-except block for critical errors (e.g., imports)
            error_info = f"A critical error occurred during batch setup:\n{str(e)}"
            self.log_queue.put(UIMessage(UIMessageType.ERROR, error_info))
            self.root.after(0, lambda: self.analyze_btn.config(state=tk.NORMAL))
