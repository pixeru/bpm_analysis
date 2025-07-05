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
        return "Please upload an audio file first.", None, None, None, None, None

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
        plotly_fig = analyze_wav_file(
            wav_file_path=wav_path,
            params=ANALYSIS_PARAMS,
            start_bpm_hint=start_bpm_hint if start_bpm_hint > 0 else None,
            original_file_path=original_file_path,
            output_directory=OUTPUTS_DIR
        )

        # Check if output files exist
        if not os.path.exists(plot_path) or not os.path.exists(summary_path):
             return "Analysis ran, but output files were not generated.", None, None, None, None, None

        # Read the content of the files
        summary_content = ""
        debug_log_content = ""
        
        # Read the summary markdown file
        if os.path.exists(summary_path):
            with open(summary_path, 'r', encoding='utf-8') as f:
                summary_content = f.read()
        
        # Read the debug log markdown file
        if os.path.exists(debug_log_path):
            with open(debug_log_path, 'r', encoding='utf-8') as f:
                debug_log_content = f.read()

        # Return the paths for Gradio to download
        downloadable_files = [plot_path, summary_path, debug_log_path]

        # Create status message
        status_html = "<p style='font-size: 1.2em; color: green;'>✅ Analysis Complete!</p>"

        return status_html, downloadable_files, plotly_fig, summary_content, debug_log_content

    except Exception as e:
        # Return the error message to the status box
        error_html = f"<p style='color: red;'>An error occurred: {str(e)}</p>"
        return error_html, None, None, None, None, None

# --- Create the Gradio Interface ---
with gr.Blocks() as demo:
    gr.Markdown("# ❤️ Heartbeat Audio Analysis")
    gr.Markdown("Upload an audio/video file to analyze the BPM and generate a report. The interactive plot and analysis results will appear below once the analysis is finished.")

    with gr.Row():
        with gr.Column(scale=1):
            audio_input = gr.File(label="Upload Audio File", file_types=[".wav", ".mp3", ".m4a", ".flac", ".ogg", ".mkv", ".avi", ".mov", ".mp4"], file_count="single")
            bpm_hint = gr.Slider(minimum=0, maximum=200, value=0, label="Starting BPM Hint (Optional)", info="If you know the approximate starting BPM, set it here. Leave at 0 to auto-detect.")
            submit_btn = gr.Button("Analyze", variant="primary")

        with gr.Column(scale=2):
            # This HTML component will display status and errors
            status_output = gr.HTML(label="Status")
            download_output = gr.File(label="Downloadable Output Files", file_count="multiple", interactive=False)

    # Results section with collapsible accordions
    with gr.Accordion("📊 Interactive BPM Analysis Plot", open=True):
        plot_output = gr.Plot(label="BPM Analysis Plot")
    
    with gr.Accordion("📋 Analysis Summary", open=True):
        summary_output = gr.Markdown(label="Summary")
    
    with gr.Accordion("🔍 Debug Log", open=True):
        debug_output = gr.Markdown(label="Debug Log")

    submit_btn.click(
        fn=run_analysis,
        inputs=[audio_input, bpm_hint],
        outputs=[status_output, download_output, plot_output, summary_output, debug_output]
    )

demo.launch()