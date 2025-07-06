import os
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output, State, ctx, dash_table
from dash.dependencies import ClientsideFunction
from scipy.io import wavfile
import glob
import dash
import io

# Import plotting functions from bpm_analysis
from bpm_analysis import preprocess_audio, _calculate_dynamic_noise_floor

def get_processed_files():
    """Get list of processed files from processed_files directory"""
    processed_dir = "processed_files"
    if not os.path.exists(processed_dir):
        print(f"Directory {processed_dir} does not exist")
        return []
    
    # Get all files that have _bpm_plot.csv
    csv_files = glob.glob(os.path.join(processed_dir, "*_bpm_plot.csv"))
    print(f"Found CSV files: {csv_files}")
    
    file_list = [os.path.basename(f).replace("_bpm_plot.csv", "") for f in csv_files]
    print(f"Available files: {file_list}")
    return file_list

def load_file_data(filename):
    """Load envelope and BPM data for a given processed file"""
    processed_dir = "processed_files"
    
    print(f"\n=== Loading data for {filename} ===")
    
    # Load BPM data from CSV
    bpm_csv_path = os.path.join(processed_dir, f"{filename}_bpm_plot.csv")
    if os.path.exists(bpm_csv_path):
        bpm_df = pd.read_csv(bpm_csv_path)
        bpm_times = bpm_df['Time (s)'].values
        bpm_values = bpm_df['Average BPM'].values
        print(f"✓ Loaded BPM data: {len(bpm_times)} points")
    else:
        print(f"✗ BPM CSV not found: {bpm_csv_path}")
        return None, None, None
    
    # Try to load envelope from filtered debug WAV file first
    filtered_wav_path = os.path.join(processed_dir, f"{filename}_filtered_debug.wav")
    print(f"Looking for filtered WAV file: {filtered_wav_path}")
    if os.path.exists(filtered_wav_path):
        print(f"✓ Found filtered debug WAV file")
        try:
            sample_rate, audio_data = wavfile.read(filtered_wav_path)
            print(f"  - Sample rate: {sample_rate} Hz")
            print(f"  - Audio data shape: {audio_data.shape}")
            print(f"  - Audio data type: {audio_data.dtype}")
            
            if audio_data.ndim > 1:
                audio_data = np.mean(audio_data, axis=1)
                print(f"  - Converted to mono: {audio_data.shape}")
            
            # Calculate envelope from filtered audio
            audio_abs = np.abs(audio_data)
            window_size = sample_rate // 10
            print(f"  - Window size for envelope: {window_size}")
            
            envelope = pd.Series(audio_abs).rolling(window=window_size, min_periods=1, center=True).mean().values
            time_axis = np.arange(len(envelope)) / sample_rate
            
            envelope_array = np.array(envelope)
            print(f"✓ Loaded envelope from {filtered_wav_path}: {len(envelope_array)} samples")
            print(f"  - Time range: {time_axis[0]:.2f}s to {time_axis[-1]:.2f}s")
            print(f"  - Envelope range: {float(np.amin(envelope_array)):.3f} to {float(np.amax(envelope_array)):.3f}")
            
        except Exception as e:
            print(f"✗ Error loading filtered WAV file {filtered_wav_path}: {e}")
            return None, None, None
    else:
        print(f"✗ Filtered WAV not found, trying processed WAV file...")
        # Fallback: try to load from processed WAV file
        wav_path = os.path.join(processed_dir, f"{filename}.wav")
        print(f"Looking for processed WAV file: {wav_path}")
        if os.path.exists(wav_path):
            print(f"✓ Found processed WAV file")
            try:
                sample_rate, audio_data = wavfile.read(wav_path)
                print(f"  - Sample rate: {sample_rate} Hz")
                print(f"  - Audio data shape: {audio_data.shape}")
                print(f"  - Audio data type: {audio_data.dtype}")
                
                if audio_data.ndim > 1:
                    audio_data = np.mean(audio_data, axis=1)
                    print(f"  - Converted to mono: {audio_data.shape}")
                
                # Calculate envelope
                audio_abs = np.abs(audio_data)
                window_size = sample_rate // 10
                print(f"  - Window size for envelope: {window_size}")
                
                envelope = pd.Series(audio_abs).rolling(window=window_size, min_periods=1, center=True).mean().values
                time_axis = np.arange(len(envelope)) / sample_rate
                
                envelope_array = np.array(envelope)
                print(f"✓ Loaded envelope from {wav_path}: {len(envelope_array)} samples")
                print(f"  - Time range: {time_axis[0]:.2f}s to {time_axis[-1]:.2f}s")
                print(f"  - Envelope range: {float(np.amin(envelope_array)):.3f} to {float(np.amax(envelope_array)):.3f}")
                
            except Exception as e:
                print(f"✗ Error loading WAV file {wav_path}: {e}")
                return None, None, None
        else:
            print(f"✗ No WAV files found for {filename}")
            return None, None, None
    
    print(f"=== Data loading complete ===\n")
    return time_axis, envelope, (bpm_times, bpm_values)

def load_labels(filename):
    """Load existing labels for a file"""
    processed_dir = "processed_files"
    labels_path = os.path.join(processed_dir, f"{filename}_labels.csv")
    if os.path.exists(labels_path):
        try:
            # Try to read the new format (with sections)
            with open(labels_path, 'r') as f:
                content = f.read()
            
            # Check if it's the new format with sections
            if "# Peak Labels" in content:
                # Find the peak labels section
                lines = content.split('\n')
                peak_labels_start = None
                peak_labels_end = None
                
                for i, line in enumerate(lines):
                    if line.strip() == "# Peak Labels":
                        peak_labels_start = i + 1
                    elif line.strip() == "# S1-S2 Intervals" and peak_labels_start is not None:
                        peak_labels_end = i
                        break
                
                if peak_labels_start is not None:
                    if peak_labels_end is not None:
                        # Extract peak labels section
                        peak_labels_lines = lines[peak_labels_start:peak_labels_end]
                    else:
                        # No intervals section, take everything after peak labels header
                        peak_labels_lines = lines[peak_labels_start:]
                    
                    # Convert back to string and read with pandas
                    peak_labels_content = '\n'.join(peak_labels_lines)
                    return pd.read_csv(io.StringIO(peak_labels_content))
                else:
                    # Fallback to old format
                    return pd.read_csv(labels_path)
            else:
                # Old format, read normally
                return pd.read_csv(labels_path)
        except Exception as e:
            print(f"Error loading labels from {labels_path}: {e}")
            # Return empty DataFrame if there's any error
            return pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
    return pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])

def save_labels(df, filename):
    """Save labels for a file"""
    processed_dir = "processed_files"
    labels_path = os.path.join(processed_dir, f"{filename}_labels.csv")
    
    # Ensure data is sorted and has limited decimal places before saving
    if not df.empty:
        df_sorted = df.sort_values("Time (s)").reset_index(drop=True)
        # Round numeric columns to 3 decimal places
        df_sorted["Time (s)"] = df_sorted["Time (s)"].round(3)
        df_sorted["Average BPM"] = df_sorted["Average BPM"].round(3)
        
        # Calculate S1-S2 intervals and add them to the CSV
        pairs = calculate_s1_s2_diffs(df_sorted)
        if pairs:
            # Create intervals DataFrame
            intervals_df = pd.DataFrame(pairs, columns=["S1_Time", "S2_Time", "Delta_t", "S1_BPM"])
            intervals_df = intervals_df.round(3)
            
            # Save both the labels and intervals
            with open(labels_path, 'w') as f:
                f.write("# Peak Labels\n")
                df_sorted.to_csv(f, index=False)
                f.write("\n# S1-S2 Intervals\n")
                intervals_df.to_csv(f, index=False)
        else:
            df_sorted.to_csv(labels_path, index=False)
    else:
        df.to_csv(labels_path, index=False)

def find_nearest_idx(array, value):
    return (np.abs(array - value)).argmin()

def calculate_s1_s2_diffs(df):
    """Calculate time differences between S1 and S2 pairs"""
    if df.empty:
        return []
    
    # Sort by time, then find S1->S2 pairs
    df_sorted = df.sort_values("Time (s)")
    s1_data = df_sorted[df_sorted["Peak Type"] == "S1"][["Time (s)", "Average BPM"]].values
    s2_times = df_sorted[df_sorted["Peak Type"] == "S2"]["Time (s)"].values
    
    pairs = []
    i, j = 0, 0
    while i < len(s1_data) and j < len(s2_times):
        if s2_times[j] > s1_data[i][0]:  # s1_data[i][0] is the time
            pairs.append((s1_data[i][0], s2_times[j], s2_times[j] - s1_data[i][0], s1_data[i][1]))  # s1_data[i][1] is the BPM
            i += 1
            j += 1
        else:
            j += 1
    return pairs

def calculate_avg_delta_t_in_range(df, start_time, end_time):
    """Calculate average S1-S2 Interval for S1-S2 pairs within a time range"""
    if df.empty or start_time is None or end_time is None:
        return None, None, []
    
    # Get all pairs
    all_pairs = calculate_s1_s2_diffs(df)
    
    # Filter pairs where S1 is within the time range
    pairs_in_range = []
    for s1_time, s2_time, delta_t, s1_bpm in all_pairs:
        if start_time <= s1_time <= end_time:
            pairs_in_range.append((s1_time, s2_time, delta_t, s1_bpm))
    
    if not pairs_in_range:
        return None, None, []
    
    # Calculate averages
    delta_ts = [pair[2] for pair in pairs_in_range]
    bpm_values = [pair[3] for pair in pairs_in_range]
    avg_delta_t = sum(delta_ts) / len(delta_ts)
    avg_bpm = sum(bpm_values) / len(bpm_values)
    
    return avg_delta_t, avg_bpm, pairs_in_range

def detect_labeling_groups(df, gap_threshold=5.0):
    """Detect groups of labelings based on time gaps between S1 peaks"""
    if df.empty:
        return []
    
    # Get all S1 peaks sorted by time
    s1_data = df[df["Peak Type"] == "S1"].sort_values("Time (s)")
    
    if len(s1_data) < 2:
        return []
    
    groups = []
    current_group = [s1_data.iloc[0]]
    
    for i in range(1, len(s1_data)):
        current_time = s1_data.iloc[i]["Time (s)"]
        previous_time = s1_data.iloc[i-1]["Time (s)"]
        
        # If gap is less than threshold, add to current group
        if current_time - previous_time < gap_threshold:
            current_group.append(s1_data.iloc[i])
        else:
            # Gap is >= threshold, finish current group and start new one
            if len(current_group) > 0:
                # Convert list to DataFrame
                groups.append(pd.DataFrame(current_group))
            current_group = [s1_data.iloc[i]]
    
    # Add the last group
    if len(current_group) > 0:
        groups.append(pd.DataFrame(current_group))
    
    return groups

def calculate_group_statistics(df, groups):
    """Calculate average S1-S2 Interval and BPM for each group"""
    if not groups:
        return []
    
    group_stats = []
    
    for i, group in enumerate(groups):
        if len(group) < 2:  # Need at least 2 S1 peaks for meaningful stats
            continue
            
        # Get time range for this group
        start_time = group.iloc[0]["Time (s)"]
        end_time = group.iloc[-1]["Time (s)"]
        
        # Calculate average Δt and BPM for this group
        avg_delta_t, avg_bpm, pairs_in_group = calculate_avg_delta_t_in_range(df, start_time, end_time)
        
        if avg_delta_t is not None:
            group_stats.append({
                'group_id': i + 1,
                'start_time': start_time,
                'end_time': end_time,
                'duration': end_time - start_time,
                's1_count': len(group),
                'avg_delta_t': avg_delta_t,
                'avg_bpm': avg_bpm,
                'pairs_count': len(pairs_in_group)
            })
    
    return group_stats

# Initialize app
app = Dash(__name__)

# Get available files
available_files = get_processed_files()

# Global cache for loaded data to avoid reloading
_data_cache = {}

app.layout = html.Div([
    # Components to initialize and store keyboard shortcut data
    dcc.Location(id='url', refresh=False),
    dcc.Store(id='keyboard-store'),
    dcc.Interval(id='keyboard-interval', interval=100, n_intervals=0),  # Poll every 100ms

    html.H2("Heartbeat Peak Labeler"),
    
    # File selector
    html.Div([
        html.Label("Select File to Label:"),
        dcc.Dropdown(
            id="file-selector",
            options=[{"label": f, "value": f} for f in available_files],
            value=available_files[0] if available_files else None,
            style={"width": "400px"}
        )
    ], style={"margin": "10px 0"}),
    
    # Main plot
    dcc.Graph(
        id="envelope-plot",
        config={
            "displayModeBar": True, 
            "scrollZoom": True, 
            "modeBarButtonsToAdd": ["pan2d"],
            "modeBarButtonsToRemove": ["select2d", "lasso2d"]
        },
        style={"height": "600px"}
    ),
    
    # Controls
    html.Div([
        html.Label("Select Peak Type:"),
        dcc.Dropdown(
            id="peak-type",
            options=[{"label": "S1", "value": "S1"}, {"label": "S2", "value": "S2"}],
            value="S1",
            style={"width": "100px", "display": "inline-block", "marginRight": "10px"}
        ),
        html.Button("Save Labels", id="save-btn", n_clicks=0),
        html.Button("Clear Labels", id="clear-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Div([
            html.P("Select S1 or S2 above, then click on the plot to add peaks.", 
                   style={"fontSize": "12px", "color": "gray", "marginTop": "5px"}),
            html.P("Keyboard shortcuts: Press 'Z' for S1, 'X' for S2", 
                   style={"fontSize": "12px", "color": "blue", "marginTop": "2px"})
        ]),
    ], style={"margin": "10px 0"}),
    
    # Labels table and S1-S2 intervals side by side
    html.Div([
        # Labels table
        html.Div([
            html.H4("Peak Labels"),
            dash_table.DataTable(
                id="labels-table",
                columns=[{"name": c, "id": c} for c in ["Time (s)", "Average BPM", "Peak Type"]],
                data=[],
                editable=True,
                row_deletable=True,
                style_table={"maxHeight": "300px", "overflowY": "auto", "width": "400px"},
            ),
        ], style={"display": "inline-block", "verticalAlign": "top", "marginRight": "20px"}),
        
        # S1-S2 intervals
        html.Div([
            html.H4("S1-S2 Intervals (s)"),
            html.Div(id="s1s2-intervals", style={"maxHeight": "300px", "overflowY": "auto"}),
        ], style={"display": "inline-block", "verticalAlign": "top"}),
    ]),
    
    # Time range analysis
    html.H4("Time Range Analysis"),
    html.Div([
        html.Label("Start Time (s):"),
        dcc.Input(
            id="start-time",
            type="number",
            placeholder="e.g., 268.0",
            style={"width": "120px", "marginRight": "10px"}
        ),
        html.Label("End Time (s):"),
        dcc.Input(
            id="end-time", 
            type="number",
            placeholder="e.g., 270.0",
            style={"width": "120px", "marginRight": "10px"}
        ),
        html.Button("Calculate Average S1-S2 Interval", id="calc-avg-btn", n_clicks=0),
        html.Div(id="avg-delta-t-output", style={"marginTop": "10px"})
    ]),
    
    # Automatic group analysis
    html.H4("Automatic Group Analysis"),
    html.Div(id="group-analysis-output"),
])

# ---- NEW KEYBOARD SHORTCUT CALLBACKS ----

# Combined clientside callback that handles both setup and periodic checking
app.clientside_callback(
    ClientsideFunction(
        namespace='keyboard',      # From assets/keyboard_shortcuts.js
        function_name='handle_keyboard_combined' # Combined function
    ),
    Output('keyboard-store', 'data'),
    Input('url', 'pathname'),         # Trigger this callback when the page loads
    Input('keyboard-interval', 'n_intervals')  # And periodically
)

# This server-side callback listens for data changes in the keyboard-store
@app.callback(
    Output("peak-type", "value"),
    Input("keyboard-store", "data"),
    prevent_initial_call=True
)
def handle_keyboard_input(keyboard_data):
    """Handle keyboard input for Z and X keys."""
    if keyboard_data and keyboard_data.get('last_key'):
        key = keyboard_data['last_key'].lower()
        if key == 'z':
            return "S1"
        elif key == 'x':
            return "S2"
    return dash.no_update

# ---- END NEW KEYBOARD SHORTCUT CALLBACKS ----


@app.callback(
    Output("envelope-plot", "figure"),
    Output("labels-table", "data"),
    Output("s1s2-intervals", "children"),
    Input("file-selector", "value"),
    Input("envelope-plot", "clickData"),
    Input("save-btn", "n_clicks"),
    Input("clear-btn", "n_clicks"),
    Input("labels-table", "data_timestamp"),
    State("labels-table", "data"),
    State("peak-type", "value")
)
def update_plot_and_labels(selected_file, clickData, save_clicks, clear_clicks, data_timestamp, table_data, peak_type):
    triggered = ctx.triggered_id
    
    if not selected_file:
        return go.Figure(), [], []
    
    # Handle initial load or file selection
    if triggered is None or triggered == "file-selector":
        # Load existing labels for new file
        df = load_labels(selected_file)
    else:
        # Use table data from the table component
        df = pd.DataFrame(table_data) if table_data else pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
    
    # Load data for selected file (use cache to avoid reloading)
    if triggered is None or triggered == "file-selector":
        print(f"Loading data for file: {selected_file}")
        time_axis, envelope, bpm_data = load_file_data(selected_file)
        if time_axis is None:
            print(f"Failed to load data for {selected_file}")
            return go.Figure(), [], []
        
        # Cache the data
        _data_cache[selected_file] = (time_axis, envelope, bpm_data)
        
        print(f"Successfully loaded data:")
        print(f"  - Time axis: {len(time_axis)} points, range {time_axis[0]:.2f}s to {time_axis[-1]:.2f}s")
        print(f"  - Envelope: {len(envelope)} points")
        if bpm_data:
            bpm_times, bpm_values = bpm_data
            print(f"  - BPM data: {len(bpm_times)} points")
        else:
            print(f"  - No BPM data available")
            bpm_times, bpm_values = [], []
    else:
        # Use cached data for other triggers
        if selected_file in _data_cache:
            time_axis, envelope, bpm_data = _data_cache[selected_file]
            if bpm_data:
                bpm_times, bpm_values = bpm_data
            else:
                bpm_times, bpm_values = [], []
        else:
            print(f"Error: No cached data for {selected_file}")
            return go.Figure(), [], []
    
    # Handle labels
    if triggered == "envelope-plot" and clickData:
        # Add new label - just get the x coordinate directly
        x = clickData["points"][0]["x"]
        print(f"Click data x value: {x}, type: {type(x)}")
        
        # Convert to float if needed
        x = float(x)
        print(f"Converted x to seconds: {x}")
        
        # Ensure the time is within the valid range
        if x < 0:
            print(f"Warning: Click time {x} is negative, clamping to 0")
            x = 0
        elif x > time_axis[-1]:
            print(f"Warning: Click time {x} is beyond data range, clamping to {time_axis[-1]}")
            x = time_axis[-1]
        
        idx = find_nearest_idx(time_axis, float(x))
        print(f"Found nearest index: {idx}, time at index: {time_axis[idx]}")
        
        # Find BPM at this time
        bpm_idx = find_nearest_idx(bpm_times, float(x))
        bpm_at_time = bpm_values[bpm_idx] if bpm_idx < len(bpm_values) else 0
        
        new_row = {
            "Time (s)": round(float(time_axis[idx]), 3), 
            "Average BPM": round(float(bpm_at_time), 3), 
            "Peak Type": peak_type
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        # Sort by time to maintain chronological order
        df = df.sort_values("Time (s)").reset_index(drop=True)
        
    elif triggered == "save-btn":
        save_labels(df, selected_file)
        
    elif triggered == "clear-btn":
        df = pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
        save_labels(df, selected_file)
    
    # Calculate S1-S2 intervals
    pairs = calculate_s1_s2_diffs(df)
    intervals = [f"S1 at {s1:.2f}s (BPM: {bpm:.1f}), S2 at {s2:.2f}s, S1-S2 Interval = {dt:.3f}s" for s1, s2, dt, bpm in pairs]
    
    # Create plot similar to _bpm_plot.html
    fig = go.Figure()
    
    # Add envelope trace
    envelope_array = np.array(envelope)
    print(f"Adding envelope trace: {len(time_axis)} time points, {len(envelope_array)} envelope points")
    print(f"Envelope range: {float(np.amin(envelope_array)):.3f} to {float(np.amax(envelope_array)):.3f}")
    
    # Check for any NaN or infinite values
    if np.any(np.isnan(envelope_array)) or np.any(np.isinf(envelope_array)):
        print("WARNING: Envelope contains NaN or infinite values!")
        envelope_array = np.nan_to_num(envelope_array, nan=0.0, posinf=0.0, neginf=0.0)
    
    # Check if envelope has any variation
    if np.amax(envelope_array) - np.amin(envelope_array) < 1e-6:
        print("WARNING: Envelope has no variation - might be flat!")
    
    # Use raw time values for x-axis
    fig.add_trace(go.Scatter(
        x=time_axis,
        y=envelope_array,
        name="Audio Envelope",
        line=dict(color="#47a5c4")
    ))
    
    # Add BPM trace on secondary y-axis
    if len(bpm_times) > 0:
        fig.add_trace(go.Scatter(
            x=bpm_times,
            y=bpm_values,
            name="Average BPM",
            line=dict(color="#4a4a4a", width=3),
            yaxis="y2"
        ))
    
    # Add manual labels
    if not df.empty:
        for label in ["S1", "S2"]:
            pts = df[df["Peak Type"] == label]
            if not pts.empty:
                # Interpolate envelope values at label times
                label_times_array = pts["Time (s)"].to_numpy()
                time_axis_array = np.array(time_axis)
                envelope_array = np.array(envelope)
                label_envelope_values = np.interp(label_times_array, time_axis_array, envelope_array)
                
                fig.add_trace(go.Scatter(
                    x=pts["Time (s)"],
                    y=label_envelope_values,
                    mode="markers",
                    name=f"Manual {label}",
                    marker=dict(
                        size=12, 
                        symbol="diamond" if label=="S1" else "circle",
                        color="#e36f6f" if label=="S1" else "orange"
                    ),
                    customdata=pts["Average BPM"],
                    hovertemplate=f"Manual {label}<br>Time: %{{x:.2f}}s<br>BPM: %{{customdata:.1f}}<extra></extra>"
                ))
    
    # Add group center hover annotations
    groups = detect_labeling_groups(df, gap_threshold=3.0)
    group_stats = calculate_group_statistics(df, groups)
    
    if group_stats:
        # Get envelope values at group centers for positioning
        group_centers = []
        group_hover_texts = []
        
        for stat in group_stats:
            center_time = (stat['start_time'] + stat['end_time']) / 2
            # Interpolate envelope value at center time
            center_envelope = np.interp(center_time, time_axis, envelope_array)
            group_centers.append((center_time, center_envelope))
            
            # Create hover text
            hover_text = f"Group {stat['group_id']}<br>"
            hover_text += f"S1-S2 Interval: {stat['avg_delta_t']:.3f}s<br>"
            hover_text += f"BPM: {stat['avg_bpm']:.1f}<br>"
            hover_text += f"Range: {stat['start_time']:.1f}s - {stat['end_time']:.1f}s<br>"
            hover_text += f"S1 peaks: {stat['s1_count']}, Pairs: {stat['pairs_count']}"
            group_hover_texts.append(hover_text)
        
        # Add invisible trace for group centers
        if group_centers:
            center_times, center_envelopes = zip(*group_centers)
            fig.add_trace(go.Scatter(
                x=center_times,
                y=center_envelopes,
                mode="markers",
                name="Group Centers",
                marker=dict(
                    size=10,  # Very small, nearly invisible
                    color="rgba(0,0,0,0.1)"  # Nearly transparent
                ),
                customdata=group_hover_texts,
                hovertemplate="%{customdata}<extra></extra>",
                showlegend=False
            ))
    
    # Configure layout similar to _bpm_plot.html
    robust_upper_limit = np.quantile(envelope_array, 0.95) if len(envelope_array) > 0 else 1
    amplitude_scale = 400.0  # Default amplitude scale factor
    
    # Prepare layout configuration
    layout_config = {
        "template": "plotly_dark",
        "title_text": f"Heartbeat Analysis - {selected_file}",
        "dragmode": 'pan',  # Default to pan mode
        "legend": dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        "margin": dict(t=140, b=100),
        "hovermode": 'x unified',
        # Configure primary y-axis for signal amplitude
        "yaxis": dict(
            title="Signal Amplitude",
            range=[0, robust_upper_limit * amplitude_scale]
        ),
        # Configure secondary y-axis for BPM
        "yaxis2": dict(
            title="BPM",
            overlaying="y",
            side="right",
            range=[50, 200],
            titlefont=dict(color="#4a4a4a"),
            tickfont=dict(color="#4a4a4a")
        )
    }
    
    # Use uirevision to preserve zoom/pan state
    if triggered == "file-selector":
        # Reset view when changing files
        layout_config["uirevision"] = selected_file
    else:
        # Preserve view for all other actions (adding/deleting labels)
        layout_config["uirevision"] = selected_file
    
    fig.update_layout(**layout_config)
    
    # Configure x-axis with time format
    if len(time_axis) > 0:
        tick_positions_sec = np.linspace(0, time_axis[-1], num=10)
        ticktext = [f"{int(s // 60):02d}:{int(s % 60):02d}" for s in tick_positions_sec]
        
        fig.update_xaxes(
            title_text="Time (seconds)",
            tickvals=tick_positions_sec,
            ticktext=ticktext,
            hoverformat='.2f'
        )
    
    return fig, df.to_dict("records"), html.Ul([html.Li(i) for i in intervals])

@app.callback(
    Output("avg-delta-t-output", "children"),
    Input("calc-avg-btn", "n_clicks"),
    State("start-time", "value"),
    State("end-time", "value"),
    State("labels-table", "data"),
    prevent_initial_call=True
)
def calculate_average_delta_t(n_clicks, start_time, end_time, table_data):
    if n_clicks is None or start_time is None or end_time is None:
        return ""
    
    # Create DataFrame from table data
    df = pd.DataFrame(table_data) if table_data else pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
    
    if df.empty:
        return html.P("No data available for calculation.", style={"color": "red"})
    
    # Calculate average Δt
    result = calculate_avg_delta_t_in_range(df, start_time, end_time)
    if result[0] is None:
        return html.P(f"No S1-S2 pairs found in time range {start_time:.3f}s to {end_time:.3f}s", style={"color": "orange"})
    
    avg_delta_t, avg_bpm, pairs_in_range = result
    
    # Create detailed output
    pairs_text = []
    for s1_time, s2_time, delta_t, s1_bpm in pairs_in_range:
        pairs_text.append(f"• S1 at {s1_time:.3f}s (BPM: {s1_bpm:.1f}) → S2 at {s2_time:.3f}s, S1-S2 Interval = {delta_t:.3f}s")
    
    return html.Div([
        html.H2(f"Average S1-S2 Interval: {avg_delta_t:.3f}s, Average BPM: {avg_bpm:.1f}", style={"fontSize": "32px", "fontWeight": "bold", "color": "#42bcf5"}),
        html.P(f"Found {len(pairs_in_range)} S1-S2 pairs in range {start_time:.3f}s to {end_time:.3f}s"),
        html.H6("Pairs included:", style={"fontSize": "12px"}),
        html.Ul([html.Li(pair, style={"fontSize": "10px"}) for pair in pairs_text])
    ])

@app.callback(
    Output("group-analysis-output", "children"),
    Input("labels-table", "data"),
    prevent_initial_call=True
)
def update_group_analysis(table_data):
    """Automatically detect groups and calculate statistics"""
    if not table_data:
        return html.P("No data available for group analysis.", style={"color": "gray"})
    
    # Create DataFrame from table data
    df = pd.DataFrame(table_data)
    
    if df.empty:
        return html.P("No data available for group analysis.", style={"color": "gray"})
    
    # Detect groups
    groups = detect_labeling_groups(df, gap_threshold=5.0)
    
    if not groups:
        return html.P("No groups detected (need at least 2 S1 peaks with <5s gaps).", style={"color": "orange"})
    
    # Calculate statistics for each group
    group_stats = calculate_group_statistics(df, groups)
    
    if not group_stats:
        return html.P("No valid groups found for analysis.", style={"color": "orange"})
    
    # Create output for each group
    group_outputs = []
    for stat in group_stats:
        group_outputs.append(html.Div([
            html.H3(f"Group {stat['group_id']}: Average S1-S2 Interval: {stat['avg_delta_t']:.3f}s, Average BPM: {stat['avg_bpm']:.1f}", 
                   style={"fontSize": "20px", "fontWeight": "bold", "color": "#42bcf5", "marginBottom": "5px"}),
            html.P(f"Time range: {stat['start_time']:.3f}s - {stat['end_time']:.3f}s (Duration: {stat['duration']:.1f}s)", 
                  style={"fontSize": "12px", "marginBottom": "2px"}),
            html.P(f"S1 peaks: {stat['s1_count']}, S1-S2 pairs: {stat['pairs_count']}", 
                  style={"fontSize": "12px", "marginBottom": "10px"})
        ], style={"border": "1px solid #ddd", "padding": "10px", "marginBottom": "10px", "borderRadius": "5px"}))
    
    return html.Div(group_outputs)

if __name__ == "__main__":
    if not available_files:
        print("No processed files found in processed_files/ directory.")
        print("Please run bpm_analysis.py first to generate some processed files.")
    else:
        print(f"Found {len(available_files)} processed files: {available_files}")
        app.run(debug=True)