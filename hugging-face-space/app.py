import gradio as gr
import os
import shutil
from huggingface_hub import HfApi
from bpm_analysis import analyze_wav_file, convert_to_wav
from config import DEFAULT_PARAMS

# --- Configuration ---
OUTPUTS_DIR = "outputs"
os.makedirs(OUTPUTS_DIR, exist_ok=True)
ANALYSIS_PARAMS = DEFAULT_PARAMS.copy()
REPO_NAME = "WolfExplode/processed_files"

def Cache_files(local_path, repo_id, auth_token):
    if not auth_token:
        return "Cache skipped: HF_TOKEN not available."

    api = HfApi()
    filename = os.path.basename(local_path)

    try:
        # Check if the file already cached
        if api.file_exists(repo_id=repo_id, filename=filename, repo_type="dataset", token=auth_token):
            return f"File already cached"
        
        # If not, cache it
        api.upload_file(
            path_or_fileobj=local_path,
            path_in_repo=filename,
            repo_id=repo_id,
            token=auth_token,
            repo_type="dataset"
        )
        return
    except Exception as e:
        return f"Caching failed. Error: {e}"

# --- Main Processing Function for Batch Operations ---
def process_audio_batch(audio_files, bpm_hint):
    """Processes a list of audio files, handling them one by one."""
    if not audio_files:
        return "Please upload one or more audio files.", None, None, [], []

    batch_statuses = []
    all_output_files = []
    plots = []
    filenames = []
    access_token = os.environ.get("HF_TOKEN")

    for i, audio_file in enumerate(audio_files):
        filename = os.path.basename(audio_file.name)
        current_status = f"--- Processing file {i+1}/{len(audio_files)}: {filename} ---"
        
        try:
            # Step 1: Upload the original input file if it's new
            upload_status = Cache_files(audio_file.name, REPO_NAME, access_token)
            current_status += f"\nCache status: {upload_status}"

            # Step 2: Perform the analysis
            base_name = os.path.splitext(filename)[0]
            wav_path = os.path.join(OUTPUTS_DIR, f"{base_name}.wav")
            
            ext = os.path.splitext(filename)[1]
            if ext.lower() != '.wav':
                if not convert_to_wav(audio_file.name, wav_path):
                    raise Exception("Audio conversion failed.")
            else:
                shutil.copy(audio_file.name, wav_path)

            plot = analyze_wav_file(
                wav_file_path=wav_path,
                params=ANALYSIS_PARAMS,
                start_bpm_hint=bpm_hint if bpm_hint > 0 else None,
                original_file_path=audio_file.name,
                output_directory=OUTPUTS_DIR
            )

            if plot is None:
                raise Exception("Analysis failed - insufficient data.")

            # Step 3: Collect results
            plot_path = os.path.join(OUTPUTS_DIR, f"{base_name}_bpm_plot.html")
            summary_path = os.path.join(OUTPUTS_DIR, f"{base_name}_Analysis_Summary.md")
            debug_path = os.path.join(OUTPUTS_DIR, f"{base_name}_Debug_Log.md")

            current_output_files = [plot_path, summary_path, debug_path]
            all_output_files.extend(current_output_files)
            plots.append(plot)
            filenames.append(filename)
            current_status += "\nAnalysis status: Success"

        except Exception as e:
            current_status += f"\nAnalysis status: FAILED ({e})"
        
        batch_statuses.append(current_status)

    final_status = "\n\n".join(batch_statuses)
    return final_status, all_output_files, plots, filenames

# --- Plot Selection Function ---
def select_plot(plots, filenames, selected_choice):
    """Returns the selected plot based on dropdown selection."""
    if not plots or not selected_choice:
        return None
    
    try:
        index = int(selected_choice.split('.')[0]) - 1
        if 0 <= index < len(plots):
            return plots[index]
    except (ValueError, IndexError):
        pass
    
    return None

def select_summary(filenames, selected_choice):
    """Returns the selected summary content based on dropdown selection."""
    if not filenames or not selected_choice:
        return "No summary available"
    
    try:
        index = int(selected_choice.split('.')[0]) - 1
        if 0 <= index < len(filenames):
            base_name = os.path.splitext(filenames[index])[0]
            summary_path = os.path.join(OUTPUTS_DIR, f"{base_name}_Analysis_Summary.md")
            
            if os.path.exists(summary_path):
                with open(summary_path, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                return f"Summary file not found: {summary_path}"
    except (ValueError, IndexError, Exception) as e:
        return f"Error reading summary: {e}"
    
    return "No summary available"

def create_dropdown_choices(plots, filenames):
    """Creates dropdown choices and sets initial selection."""
    if not plots or not filenames:
        return gr.Dropdown(choices=[], value=None), None
    
    choices = [f"{i+1}. {filename}" for i, filename in enumerate(filenames)]
    initial_value = choices[0] if choices else None
    initial_plot = plots[0] if plots else None
    
    return gr.Dropdown(choices=choices, value=initial_value), initial_plot

def create_summary_dropdown_choices(filenames):
    """Creates dropdown choices for summary selection and sets initial summary."""
    if not filenames:
        return gr.Dropdown(choices=[], value=None), "No summary available"
    
    choices = [f"{i+1}. {filename}" for i, filename in enumerate(filenames)]
    initial_value = choices[0] if choices else None
    
    # Get initial summary content
    initial_summary = "No summary available"
    if initial_value:
        try:
            index = int(initial_value.split('.')[0]) - 1
            if 0 <= index < len(filenames):
                base_name = os.path.splitext(filenames[index])[0]
                summary_path = os.path.join(OUTPUTS_DIR, f"{base_name}_Analysis_Summary.md")
                
                if os.path.exists(summary_path):
                    with open(summary_path, 'r', encoding='utf-8') as f:
                        initial_summary = f.read()
        except Exception:
            pass
    
    return gr.Dropdown(choices=choices, value=initial_value), initial_summary

# --- Create the Gradio Interface ---
with gr.Blocks(css="""
    .large-plot {
        min-height: 800px !important;
        height: 800px !important;
    }
    .large-plot svg.main-svg {
        height: 800px !important;
        min-height: 800px !important;
    }
    .large-plot .js-plotly-plot {
        height: 800px !important;
        min-height: 800px !important;
    }
""") as app:
    gr.Markdown("# ❤️ Heartbeat Audio Analysis")
    gr.Markdown("Upload one or more audio files to analyze heart rate patterns")
    
    with gr.Row():
        with gr.Column():
            # Allow multiple files to be uploaded
            audio_input = gr.File(label="Audio File(s)", file_types=["audio", "video"], file_count="multiple")
            bpm_hint = gr.Slider(minimum=0, maximum=200, value=0, label="Initial BPM Estimate (Optional)")
            analyze_btn = gr.Button("Run Analysis", variant="primary")
        with gr.Column():
            status_output = gr.Textbox(label="Processing Status", lines=10, interactive=False)

    with gr.Tab("📁 Results Download"):
        gr.Markdown("All generated plots, summaries, and logs from the batch run will be available for download here.")
        file_output = gr.File(label="Analysis Files", file_count="multiple", interactive=False)
        
    with gr.Tab("📊 Visualization"):
        gr.Markdown("""
        **Note:** Select which file's plot to display from the dropdown below. 
        For full interactive features, download the individual HTML files and open them in your browser.
        """)
        with gr.Row():
            plot_selector = gr.Dropdown(
                label="Select File to Display",
                choices=[],
                interactive=True,
                value=None
            )
        plot_display = gr.Plot(label="Heart Rate Analysis", container=True, elem_classes=["large-plot"])
    
    with gr.Tab("📋 Analysis Summary"):
        gr.Markdown("""
        **Note:** Select which file's analysis summary to display from the dropdown below.
        """)
        with gr.Row():
            summary_selector = gr.Dropdown(
                label="Select File Summary to Display",
                choices=[],
                interactive=True,
                value=None
            )
        summary_display = gr.Markdown(label="Analysis Summary", value="No summary available")
    
    # Hidden components to store plots and filenames
    plots_state = gr.State([])
    filenames_state = gr.State([])
    
    # Event handlers
    analyze_btn.click(
        fn=process_audio_batch,
        inputs=[audio_input, bpm_hint],
        outputs=[status_output, file_output, plots_state, filenames_state]
    ).then(
        fn=create_dropdown_choices,
        inputs=[plots_state, filenames_state],
        outputs=[plot_selector, plot_display]
    ).then(
        fn=create_summary_dropdown_choices,
        inputs=[filenames_state],
        outputs=[summary_selector, summary_display]
    )
    
    plot_selector.change(
        fn=select_plot,
        inputs=[plots_state, filenames_state, plot_selector],
        outputs=plot_display
    )
    
    summary_selector.change(
        fn=select_summary,
        inputs=[filenames_state, summary_selector],
        outputs=summary_display
    )

app.launch()