import gradio as gr
import os
import shutil
from pathlib import Path # Import the Path object for easier path handling
from bpm_analysis import analyze_wav_file, convert_to_wav
from config import DEFAULT_PARAMS

# Create a permanent output directory
OUTPUTS_DIR = "outputs"
os.makedirs(OUTPUTS_DIR, exist_ok=True)

ANALYSIS_PARAMS = DEFAULT_PARAMS.copy()

def run_analysis(audio_file, start_bpm_hint):
    if audio_file is None:
        return "Please upload an audio file first.", None, None

    try:
        # The Gradio File component gives us an object with a .name attribute
        original_file_path = audio_file.name
        base_name = os.path.basename(os.path.splitext(original_file_path)[0])

        # Define specific output paths in our permanent 'outputs' directory
        plot_path = os.path.join(OUTPUTS_DIR, f"{base_name}_bpm_plot.html")
        summary_path = os.path.join(OUTPUTS_DIR, f"{base_name}_Analysis_Summary.md")
        debug_log_path = os.path.join(OUTPUTS_DIR, f"{base_name}_Debug_Log.md")
        wav_path = os.path.join(OUTPUTS_DIR, f"{os.path.basename(base_name)}.wav")

        # Handle file conversion if necessary
        ext = os.path.splitext(original_file_path)[1]
        if ext.lower() != '.wav':
            if not convert_to_wav(original_file_path, wav_path):
                raise Exception("File conversion to WAV failed.")
        else:
            # If it's already a .wav, just copy it to our output dir
            shutil.copy(original_file_path, wav_path)

        # Run the main analysis function
        analyze_wav_file(
            wav_file_path=wav_path,
            params=ANALYSIS_PARAMS,
            start_bpm_hint=start_bpm_hint if start_bpm_hint > 0 else None,
            original_file_path=original_file_path,
            output_directory=OUTPUTS_DIR
        )

        # Check if output files exist
        if not os.path.exists(plot_path) or not os.path.exists(summary_path):
             return "Analysis ran, but output files were not generated.", None, None

        # Return the paths for Gradio to display and download
        downloadable_files = [plot_path, summary_path, debug_log_path]

        # --- THIS IS THE FIX ---
        # Convert the file path to a URL-friendly format with forward slashes
        url_friendly_path = str(Path(plot_path)).replace('\\', '/')

        # Create an HTML link for the plot that opens in a new tab
        plot_link_html = f"""
        <p style='font-size: 1.2em;'>
            ✅ Analysis Complete!
            <a href="/file={url_friendly_path}" target="_blank" style='margin-left: 20px; font-weight: bold; text-decoration: underline;'>
                Click here to open the interactive plot in a new tab.
            </a>
        </p>
        """

        return plot_link_html, downloadable_files

    except Exception as e:
        # Return the error message to the status box
        error_html = f"<p style='color: red;'>An error occurred: {str(e)}</p>"
        return error_html, None

# --- Create the Gradio Interface ---
with gr.Blocks() as demo:
    gr.Markdown("# ❤️ Heartbeat Audio Analysis")
    gr.Markdown("Upload an audio/video file to analyze the BPM and generate a report. The interactive plot will appear as a link below once the analysis is finished.")

    with gr.Row():
        with gr.Column(scale=1):
            audio_input = gr.File(label="Upload Audio File", file_types=[".wav", ".mp3", ".m4a", ".flac", ".ogg", ".mkv", ".avi", ".mov", ".mp4"], file_count="single")
            bpm_hint = gr.Slider(minimum=0, maximum=200, value=0, label="Starting BPM Hint (Optional)", info="If you know the approximate starting BPM, set it here. Leave at 0 to auto-detect.")
            submit_btn = gr.Button("Analyze", variant="primary")

        with gr.Column(scale=2):
            # This HTML component will display status, errors, and the final link
            status_and_plot_link_output = gr.HTML(label="Status")
            download_output = gr.File(label="Downloadable Output Files", file_count="multiple", interactive=False)

    submit_btn.click(
        fn=run_analysis,
        inputs=[audio_input, bpm_hint],
        outputs=[status_and_plot_link_output, download_output]
    )

demo.launch()