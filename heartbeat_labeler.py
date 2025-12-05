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
import base64

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

def detect_consecutive_same_type_labels(df):
    """Detect consecutive labels of the same type (S1-S1 or S2-S2)"""
    if df.empty or len(df) < 2:
        return []
    
    # Sort by time
    df_sorted = df.sort_values("Time (s)").reset_index(drop=True)
    
    warnings = []
    for i in range(len(df_sorted) - 1):
        current_type = df_sorted.iloc[i]["Peak Type"]
        next_type = df_sorted.iloc[i + 1]["Peak Type"]
        
        if current_type == next_type:
            current_time = df_sorted.iloc[i]["Time (s)"]
            next_time = df_sorted.iloc[i + 1]["Time (s)"]
            warnings.append({
                'time': current_time,
                'type': current_type,
                'next_time': next_time
            })
    
    return warnings

def detect_labels_too_close(df, group_stats):
    """Detect labels that are too close together (< 70% of average interval)"""
    if df.empty or len(df) < 2 or not group_stats:
        return []
    
    # Sort by time
    df_sorted = df.sort_values("Time (s)").reset_index(drop=True)
    
    warnings = []
    for i in range(len(df_sorted) - 1):
        current_time = df_sorted.iloc[i]["Time (s)"]
        current_type = df_sorted.iloc[i]["Peak Type"]
        next_time = df_sorted.iloc[i + 1]["Time (s)"]
        next_type = df_sorted.iloc[i + 1]["Peak Type"]
        
        interval = next_time - current_time
        
        # Find which group this label pair belongs to
        relevant_group = None
        for group in group_stats:
            if group['start_time'] <= current_time <= group['end_time']:
                relevant_group = group
                break
        
        if relevant_group is None:
            continue
        
        # Determine which average interval to use based on the label types
        if current_type == "S1" and next_type == "S2":
            # S1-S2 pair, use S1-S2 average
            avg_interval = relevant_group.get('avg_delta_t')
        elif current_type == "S2" and next_type == "S1":
            # S2-S1 pair, use S2-S1 average
            avg_interval = relevant_group.get('avg_s2_s1_delta_t')
        else:
            # Same type or other combinations, skip
            continue
        
        if avg_interval is None or avg_interval <= 0:
            continue
        
        # Check if interval is less than 70% of average
        threshold = 0.7 * avg_interval
        if interval < threshold:
            warnings.append({
                'time': current_time,
                'next_time': next_time,
                'interval': interval,
                'avg_interval': avg_interval,
                'threshold': threshold,
                'type_pair': f"{current_type}-{next_type}"
            })
    
    return warnings

def calculate_temporary_intervals(df):
    """Calculate time intervals between consecutive temporary labels"""
    if df.empty:
        return []
    
    # Get all temporary labels sorted by time
    temp_labels = df[df["Peak Type"] == "Temporary"].sort_values("Time (s)").reset_index(drop=True)
    
    if len(temp_labels) < 2:
        return []
    
    intervals = []
    for i in range(len(temp_labels) - 1):
        time1 = temp_labels.iloc[i]["Time (s)"]
        time2 = temp_labels.iloc[i + 1]["Time (s)"]
        interval = time2 - time1
        intervals.append({
            'time1': time1,
            'time2': time2,
            'interval': interval,
            'mid_time': (time1 + time2) / 2
        })
    
    return intervals

def get_temporary_label_range(df):
    """Get the time range between the first and last temporary labels if exactly 2 exist"""
    if df.empty:
        return None
    
    # Get all temporary labels sorted by time
    temp_labels = df[df["Peak Type"] == "Temporary"].sort_values("Time (s)").reset_index(drop=True)
    
    if len(temp_labels) != 2:
        return None
    
    return {
        'start_time': temp_labels.iloc[0]["Time (s)"],
        'end_time': temp_labels.iloc[1]["Time (s)"]
    }

def swap_s1_s2_between_temporary_labels(df):
    """Swap S1 and S2 labels that fall between two temporary labels"""
    if df.empty:
        return df
    
    # Get the time range between temporary labels
    temp_range = get_temporary_label_range(df)
    if temp_range is None:
        return df
    
    # Create a copy to avoid modifying the original
    df_copy = df.copy()
    
    # Find labels between the temporary labels (inclusive boundaries)
    time_mask = (df_copy["Time (s)"] >= temp_range['start_time']) & \
                (df_copy["Time (s)"] <= temp_range['end_time'])
    
    # Get S1 labels in range
    s1_mask = time_mask & (df_copy["Peak Type"] == "S1")
    # Get S2 labels in range
    s2_mask = time_mask & (df_copy["Peak Type"] == "S2")
    
    # Swap S1 -> S2 and S2 -> S1
    df_copy.loc[s1_mask, "Peak Type"] = "S2"
    df_copy.loc[s2_mask, "Peak Type"] = "S1"
    
    return df_copy

def delete_labels_between_temporary_labels(df):
    """Delete all S1 and S2 labels that fall between two temporary labels (keep temporary labels)"""
    if df.empty:
        return df
    
    # Get the time range between temporary labels
    temp_range = get_temporary_label_range(df)
    if temp_range is None:
        return df
    
    # Create a copy to avoid modifying the original
    df_copy = df.copy()
    
    # Find labels between the temporary labels (inclusive boundaries) that are S1 or S2
    time_mask = (df_copy["Time (s)"] >= temp_range['start_time']) & \
                (df_copy["Time (s)"] <= temp_range['end_time'])
    
    # Get S1 and S2 labels in range (exclude temporary labels)
    labels_to_delete = time_mask & (df_copy["Peak Type"].isin(["S1", "S2"]))
    
    # Delete those labels
    df_copy = df_copy[~labels_to_delete].reset_index(drop=True)
    
    return df_copy

def parse_csv_content(contents, filename):
    """Parse uploaded CSV file content"""
    try:
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        
        # Check if CSV has the expected format
        if 'Time (s)' in df.columns and 'Average BPM' in df.columns:
            return {
                'filename': filename,
                'times': df['Time (s)'].values.tolist(),
                'bpm': df['Average BPM'].values.tolist()
            }
        else:
            return None
    except Exception as e:
        print(f"Error parsing CSV {filename}: {e}")
        return None

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

def calculate_s2_s1_diffs(df):
    """Calculate time differences between S2 and S1 pairs"""
    if df.empty:
        return []
    
    # Sort by time, then find S2->S1 pairs
    df_sorted = df.sort_values("Time (s)")
    s2_data = df_sorted[df_sorted["Peak Type"] == "S2"][["Time (s)", "Average BPM"]].values
    s1_times = df_sorted[df_sorted["Peak Type"] == "S1"]["Time (s)"].values
    
    pairs = []
    i, j = 0, 0
    while i < len(s2_data) and j < len(s1_times):
        if s1_times[j] > s2_data[i][0]:  # s2_data[i][0] is the time
            pairs.append((s2_data[i][0], s1_times[j], s1_times[j] - s2_data[i][0], s2_data[i][1]))  # s2_data[i][1] is the BPM
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

def calculate_avg_s2_s1_delta_t_in_range(df, start_time, end_time):
    """Calculate average S2-S1 Interval for S2-S1 pairs within a time range"""
    if df.empty or start_time is None or end_time is None:
        return None, None, []
    
    # Get all pairs
    all_pairs = calculate_s2_s1_diffs(df)
    
    # Filter pairs where S2 is within the time range
    pairs_in_range = []
    for s2_time, s1_time, delta_t, s2_bpm in all_pairs:
        if start_time <= s2_time <= end_time:
            pairs_in_range.append((s2_time, s1_time, delta_t, s2_bpm))
    
    if not pairs_in_range:
        return None, None, []
    
    # Calculate averages
    delta_ts = [pair[2] for pair in pairs_in_range]
    bpm_values = [pair[3] for pair in pairs_in_range]
    avg_delta_t = sum(delta_ts) / len(delta_ts)
    avg_bpm = sum(bpm_values) / len(bpm_values)
    
    return avg_delta_t, avg_bpm, pairs_in_range

def detect_labeling_groups(df, gap_threshold=1):
    """Detect groups of labelings based on time gap (seconds) between S1 peaks"""
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
    """Calculate average S1-S2 and S2-S1 Intervals and BPM for each group"""
    if not groups:
        return []
    
    group_stats = []
    
    for i, group in enumerate(groups):
        if len(group) < 2:  # Need at least 2 S1 peaks for meaningful stats
            continue
            
        # Get time range for this group
        start_time = group.iloc[0]["Time (s)"]
        end_time = group.iloc[-1]["Time (s)"]
        
        # Calculate average S1-S2 Δt and BPM for this group
        avg_delta_t, avg_bpm, pairs_in_group = calculate_avg_delta_t_in_range(df, start_time, end_time)
        
        # Calculate average S2-S1 Δt and BPM for this group
        avg_s2_s1_delta_t, avg_s2_s1_bpm, s2_s1_pairs_in_group = calculate_avg_s2_s1_delta_t_in_range(df, start_time, end_time)
        
        if avg_delta_t is not None:
            group_stats.append({
                'group_id': i + 1,
                'start_time': start_time,
                'end_time': end_time,
                'duration': end_time - start_time,
                's1_count': len(group),
                'avg_delta_t': avg_delta_t,  # S1-S2 interval
                'avg_bpm': avg_bpm,
                'pairs_count': len(pairs_in_group),
                'avg_s2_s1_delta_t': avg_s2_s1_delta_t,  # S2-S1 interval
                'avg_s2_s1_bpm': avg_s2_s1_bpm,
                's2_s1_pairs_count': len(s2_s1_pairs_in_group) if s2_s1_pairs_in_group else 0
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

    # ADD A HIDDEN BUTTON TO TRIGGER UNDO
    html.Button(id='undo-trigger', n_clicks=0, style={'display': 'none'}),
    
    # ADD A HIDDEN STORE TO TRACK UNDO HISTORY
    dcc.Store(id='undo-history', data=[]),
    
    # Store for comparison CSV data
    dcc.Store(id='comparison-csv-data', data=[]),
    
    # Download component for CSV export
    dcc.Download(id="download-csv"),

    html.H2("Heartbeat Peak Labeler"),
    
    # File selector
    html.Div([
        html.Label("Select File to Label:"),
        dcc.Dropdown(
            id="file-selector",
            options=[{"label": f, "value": f} for f in available_files],
            value=available_files[0] if available_files else None,
            style={
                "width": "800px",
                "minWidth": "600px",
                "maxWidth": "1200px"
            }
        )
    ], style={"margin": "10px 0"}),
    
    # CSV comparison upload
    html.Div([
        html.Label("Load CSV Files for Comparison (BPM/Time format):"),
        dcc.Upload(
            id='upload-csv',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select CSV Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px 0',
                'cursor': 'pointer'
            },
            multiple=True
        ),
        html.Div(id='upload-status', style={"margin": "5px 0", "fontSize": "12px", "color": "gray"}),
        html.Button("Clear Comparison Data", id="clear-comparison-btn", n_clicks=0, style={"marginTop": "5px"})
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
            options=[{"label": "S1", "value": "S1"}, {"label": "S2", "value": "S2"}, {"label": "Temporary", "value": "Temporary"}],
            value="S1",
            style={"width": "100px", "display": "inline-block", "marginRight": "10px"}
        ),
        html.Button("Save Labels", id="save-btn", n_clicks=0),
        html.Button("Clear Labels", id="clear-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Button("Restore Labels from File", id="restore-labels-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Button("Swap S1/S2 Between Temporary Labels", id="swap-s1s2-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Button("Delete Labels Between Temporary Labels", id="delete-between-temp-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Button("Clear Temporary Labels", id="clear-temp-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Button("Export Labels bpm/time CSV", id="export-csv-btn", n_clicks=0, style={"marginLeft": "10px"}),
        html.Div([
            html.P("Select S1, S2, or Temporary above, then click on the plot to add peaks.", 
                   style={"fontSize": "12px", "color": "gray", "marginTop": "5px"}),
            html.P("Keyboard shortcuts: Press 'Z' for S1, 'X' for S2. Press Ctrl+Z to undo (supports multiple undos).", 
                   style={"fontSize": "12px", "color": "grey", "marginTop": "2px"}),
            html.P("Temporary labels: Use to measure time intervals between two points. Info boxes show the interval.", 
                   style={"fontSize": "12px", "color": "grey", "marginTop": "2px"}),
            html.P("Temporary label tools: Place 2 temporary labels, then use 'Swap S1/S2' or 'Delete Labels' to modify labels in that range.", 
                   style={"fontSize": "12px", "color": "grey", "marginTop": "2px"}),
            html.P("⚠️ Important: Labels are NOT saved automatically. Click 'Save Labels' to save your work!", 
                   style={"fontSize": "12px", "color": "orange", "marginTop": "2px", "fontWeight": "bold"})
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

# ---- KEYBOARD SHORTCUT CALLBACKS ----

# This clientside callback sets up the main keyboard listener
app.clientside_callback(
    ClientsideFunction(
        namespace='keyboard',
        function_name='handle_keyboard_combined'
    ),
    Output('keyboard-store', 'data'),
    Input('url', 'pathname'),
    Input('keyboard-interval', 'n_intervals')
)

# This callback updates the S1/S2 dropdown when Z or X is pressed
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

# This callback "clicks" the hidden undo button when Ctrl+Z is pressed
@app.callback(
    Output('undo-trigger', 'n_clicks'),
    Input('keyboard-store', 'data'),
    State('undo-trigger', 'n_clicks'),
    prevent_initial_call=True
)
def trigger_undo_from_keyboard(keyboard_data, n_clicks):
    if keyboard_data and keyboard_data.get('last_key') == 'ctrl+z':
        return (n_clicks or 0) + 1
    return dash.no_update

# ---- CSV UPLOAD CALLBACK ----
@app.callback(
    Output('comparison-csv-data', 'data'),
    Output('upload-status', 'children'),
    Input('upload-csv', 'contents'),
    Input('clear-comparison-btn', 'n_clicks'),
    State('comparison-csv-data', 'data'),
    State('upload-csv', 'filename'),
    prevent_initial_call=True
)
def handle_csv_upload(contents, clear_clicks, existing_data, filenames):
    triggered = ctx.triggered_id
    
    if triggered == 'clear-comparison-btn':
        return [], html.Div("Comparison data cleared.", style={"color": "green"})
    
    if not contents:
        return dash.no_update, dash.no_update
    
    if existing_data is None:
        existing_data = []
    
    # Parse uploaded files
    new_data = []
    if isinstance(contents, list):
        for content, filename in zip(contents, filenames):
            parsed = parse_csv_content(content, filename)
            if parsed:
                new_data.append(parsed)
    else:
        parsed = parse_csv_content(contents, filenames)
        if parsed:
            new_data.append(parsed)
    
    if new_data:
        # Combine with existing data
        combined_data = existing_data + new_data
        status_text = f"Loaded {len(new_data)} CSV file(s): {', '.join([d['filename'] for d in new_data])}"
        return combined_data, html.Div(status_text, style={"color": "green"})
    else:
        return dash.no_update, html.Div("Failed to parse CSV file(s). Expected format: Time (s), Average BPM", style={"color": "red"})

# ---- CSV EXPORT CALLBACK ----
@app.callback(
    Output("download-csv", "data"),
    Input("export-csv-btn", "n_clicks"),
    State("labels-table", "data"),
    State("file-selector", "value"),
    prevent_initial_call=True
)
def export_labels_to_csv(n_clicks, table_data, selected_file):
    """Export labels as CSV in the same format as bpm_analysis.py output"""
    if not table_data or not selected_file:
        return None
    
    # Convert to DataFrame
    df = pd.DataFrame(table_data)
    
    if df.empty:
        return None
    
    # Exclude temporary labels from export
    df = df[df["Peak Type"] != "Temporary"]
    
    if df.empty:
        return None
    
    # Sort by time and select only Time and BPM columns
    df_sorted = df.sort_values("Time (s)")[["Time (s)", "Average BPM"]].copy()
    
    # Round to 3 decimal places to match bpm_analysis.py format
    df_sorted["Time (s)"] = df_sorted["Time (s)"].round(3)
    df_sorted["Average BPM"] = df_sorted["Average BPM"].round(3)
    
    # Create CSV content
    csv_string = df_sorted.to_csv(index=False)
    
    # Generate filename
    filename = f"{selected_file}_labels_export.csv"
    
    return dict(content=csv_string, filename=filename)


# ---- MAIN CALLBACK ----

@app.callback(
    Output("envelope-plot", "figure"),
    Output("labels-table", "data"),
    Output("s1s2-intervals", "children"),
    Output("undo-history", "data"),
    Input("file-selector", "value"),
    Input("envelope-plot", "clickData"),
    Input("save-btn", "n_clicks"),
    Input("clear-btn", "n_clicks"),
    Input("restore-labels-btn", "n_clicks"),
    Input("swap-s1s2-btn", "n_clicks"),
    Input("delete-between-temp-btn", "n_clicks"),
    Input("clear-temp-btn", "n_clicks"),
    Input('undo-trigger', 'n_clicks'),
    Input('comparison-csv-data', 'data'),
    State("labels-table", "data"),
    State("labels-table", "data_timestamp"),
    State("peak-type", "value"),
    State("undo-history", "data")
)
def update_plot_and_labels(selected_file, clickData, save_clicks, clear_clicks, restore_clicks, swap_clicks, delete_between_clicks, clear_temp_clicks, undo_clicks, comparison_data, table_data, data_timestamp, peak_type, undo_history):
    triggered = ctx.triggered_id
    
    if not selected_file:
        return go.Figure(), [], []
    
    # Initialize undo history if None
    if undo_history is None:
        undo_history = []
    
    # Optimize: If only comparison data changed, we can skip most processing
    only_comparison_changed = (triggered == 'comparison-csv-data')
    
    # Handle initial load, file selection, or restore
    if triggered is None or triggered == "file-selector" or triggered == "restore-labels-btn":
        if triggered == "restore-labels-btn":
            df = load_labels(selected_file)
            undo_history = []  # Clear undo history when restoring labels
        else:
            df = load_labels(selected_file)
            undo_history = []  # Clear undo history when loading a new file
    elif only_comparison_changed:
        # Only comparison data changed - use current table data without reloading from file
        df = pd.DataFrame(table_data) if table_data else pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
    else:
        df = pd.DataFrame(table_data) if table_data else pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
    
    # Load data for selected file (use cache to avoid reloading)
    if triggered is None or triggered == "file-selector":
        print(f"Loading data for file: {selected_file}")
        time_axis, envelope, bpm_data = load_file_data(selected_file)
        if time_axis is None:
            print(f"Failed to load data for {selected_file}")
            return go.Figure(), [], []
        
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
        if selected_file in _data_cache:
            time_axis, envelope, bpm_data = _data_cache[selected_file]
            if bpm_data:
                bpm_times, bpm_values = bpm_data
            else:
                bpm_times, bpm_values = [], []
        else:
            print(f"Error: No cached data for {selected_file}")
            return go.Figure(), [], []
    
    # Handle label modifications (skip if only comparison data changed)
    if triggered == "envelope-plot" and clickData and not only_comparison_changed:
        x = clickData["points"][0]["x"]
        x = float(x)
        
        if x < 0: x = 0
        elif x > time_axis[-1]: x = time_axis[-1]
        
        idx = find_nearest_idx(time_axis, float(x))
        bpm_idx = find_nearest_idx(bpm_times, float(x))
        bpm_at_time = bpm_values[bpm_idx] if bpm_idx < len(bpm_values) else 0
        
        new_row = {
            "Time (s)": round(float(time_axis[idx]), 3), 
            "Average BPM": round(float(bpm_at_time), 3), 
            "Peak Type": peak_type
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df = df.sort_values("Time (s)").reset_index(drop=True)
        
        # Add the newly added label to undo history
        undo_history.append({
            "Time (s)": new_row["Time (s)"],
            "Average BPM": new_row["Average BPM"],
            "Peak Type": new_row["Peak Type"]
        })
        
        # Limit undo history to last 20 actions to prevent memory issues
        if len(undo_history) > 20:
            undo_history = undo_history[-20:]
        
    elif triggered == "save-btn":
        save_labels(df, selected_file)
        
    elif triggered == "clear-btn":
        df = pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
        undo_history = []  # Clear undo history when clearing all labels
        # Note: Labels are NOT automatically saved - user must click "Save Labels" to save
    
    elif triggered == "swap-s1s2-btn":
        # Swap S1 and S2 labels between temporary labels
        df = swap_s1_s2_between_temporary_labels(df)
        # Note: Labels are NOT automatically saved - user must click "Save Labels" to save
    
    elif triggered == "delete-between-temp-btn":
        # Delete all S1 and S2 labels between temporary labels
        df = delete_labels_between_temporary_labels(df)
        # Note: Labels are NOT automatically saved - user must click "Save Labels" to save
    
    elif triggered == "clear-temp-btn":
        # Remove only temporary labels
        df = df[df["Peak Type"] != "Temporary"].reset_index(drop=True)
        # Note: Labels are NOT automatically saved - user must click "Save Labels" to save

    # UPDATE UNDO LOGIC TO REMOVE LAST ADDED LABEL FROM HISTORY
    elif triggered == 'undo-trigger':
        if not df.empty and undo_history:
            # Get the last added label from history
            last_added_label = undo_history.pop()
            
            # Remove the label with the specific timestamp and type
            df = df[
                ~((df["Time (s)"] == last_added_label["Time (s)"]) & 
                  (df["Average BPM"] == last_added_label["Average BPM"]) & 
                  (df["Peak Type"] == last_added_label["Peak Type"]))
            ].reset_index(drop=True)
    
    # Calculate S1-S2 intervals (exclude temporary labels)
    df_non_temp = df[df["Peak Type"] != "Temporary"]
    pairs = calculate_s1_s2_diffs(df_non_temp)
    intervals = [f"S1 at {s1:.2f}s (BPM: {bpm:.1f}), S2 at {s2:.2f}s, S1-S2 Interval = {dt:.3f}s" for s1, s2, dt, bpm in pairs]
    
    # Calculate S2-S1 intervals (exclude temporary labels)
    s2_s1_pairs = calculate_s2_s1_diffs(df_non_temp)
    s2_s1_intervals = [f"S2 at {s2:.2f}s (BPM: {bpm:.1f}), S1 at {s1:.2f}s, S2-S1 Interval = {dt:.3f}s" for s2, s1, dt, bpm in s2_s1_pairs]
    intervals.extend(s2_s1_intervals)
    
    # Create plot
    fig = go.Figure()
    envelope_array = np.array(envelope)
    
    if np.any(np.isnan(envelope_array)) or np.any(np.isinf(envelope_array)):
        envelope_array = np.nan_to_num(envelope_array, nan=0.0, posinf=0.0, neginf=0.0)
    
    fig.add_trace(go.Scatter(
        x=time_axis,
        y=envelope_array,
        name="Audio Envelope",
        line=dict(color="#47a5c4")
    ))
    
    if len(bpm_times) > 0:
        fig.add_trace(go.Scatter(
            x=bpm_times,
            y=bpm_values,
            name="Average BPM",
            line=dict(color="#4a4a4a", width=3),
            yaxis="y2"
        ))
    
    # Add comparison CSV data
    if comparison_data:
        colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#f9ca24', '#6c5ce7', '#a29bfe']
        for i, csv_data in enumerate(comparison_data):
            if csv_data and 'times' in csv_data and 'bpm' in csv_data:
                color = colors[i % len(colors)]
                fig.add_trace(go.Scatter(
                    x=csv_data['times'],
                    y=csv_data['bpm'],
                    name=f"Comparison: {csv_data.get('filename', f'CSV {i+1}')}",
                    line=dict(color=color, width=2),
                    yaxis="y2"
                ))
    
    # Add manual labels
    if not df.empty:
        for label in ["S1", "S2"]:
            pts = df[df["Peak Type"] == label]
            if not pts.empty:
                label_times_array = pts["Time (s)"].to_numpy()
                label_envelope_values = np.interp(label_times_array, np.array(time_axis), envelope_array)
                
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
        
        # Add temporary labels
        temp_pts = df[df["Peak Type"] == "Temporary"]
        if not temp_pts.empty:
            temp_times_array = temp_pts["Time (s)"].to_numpy()
            temp_envelope_values = np.interp(temp_times_array, np.array(time_axis), envelope_array)
            
            fig.add_trace(go.Scatter(
                x=temp_pts["Time (s)"],
                y=temp_envelope_values,
                mode="markers",
                name="Temporary",
                marker=dict(
                    size=10,
                    symbol="x",
                    color="#9b59b6",
                    line=dict(width=2, color="#9b59b6")
                ),
                hovertemplate="Temporary<br>Time: %{x:.2f}s<extra></extra>"
            ))
            
            # Calculate and display intervals between temporary labels
            temp_intervals = calculate_temporary_intervals(df)
            for interval_info in temp_intervals:
                mid_time = interval_info['mid_time']
                mid_envelope = np.interp(mid_time, time_axis, envelope_array)
                interval_text = f"Δt = {interval_info['interval']:.3f}s"
                
                # Add info box annotation
                fig.add_annotation(
                    x=mid_time,
                    y=mid_envelope,
                    text=interval_text,
                    showarrow=True,
                    arrowhead=2,
                    arrowsize=1.5,
                    arrowwidth=2,
                    arrowcolor="#9b59b6",
                    ax=0,
                    ay=-40,
                    font=dict(color="#9b59b6", size=11, family="Arial Black"),
                    bgcolor="rgba(155, 89, 182, 0.2)",
                    bordercolor="#9b59b6",
                    borderwidth=2,
                    borderpad=4
                )
    
    # Check for consecutive same-type labels and add warnings (exclude temporary labels)
    # Skip warning calculations if only comparison data changed
    if not only_comparison_changed:
        df_non_temp = df[df["Peak Type"] != "Temporary"]
        consecutive_warnings = detect_consecutive_same_type_labels(df_non_temp)
    else:
        consecutive_warnings = []
    if consecutive_warnings:
        for warning in consecutive_warnings:
            warning_time = warning['time']
            warning_type = warning['type']
            # Find the envelope value at this time for positioning
            warning_envelope = np.interp(warning_time, time_axis, envelope_array)
            
            # Add a small, non-intrusive annotation
            fig.add_annotation(
                x=warning_time,
                y=warning_envelope,
                text=f"⚠ {warning_type}-{warning_type}",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=1,
                arrowcolor="yellow",
                ax=0,
                ay=-30,
                font=dict(color="yellow", size=9),
                bgcolor="rgba(0,0,0,0.5)",
                bordercolor="yellow",
                borderwidth=1,
                borderpad=2
            )
    
    # Add group center hover annotations (exclude temporary labels)
    groups = detect_labeling_groups(df_non_temp, gap_threshold=3.0)
    group_stats = calculate_group_statistics(df_non_temp, groups)
    
    # Check for labels that are too close together (exclude temporary labels)
    too_close_warnings = detect_labels_too_close(df_non_temp, group_stats)
    if too_close_warnings:
        for warning in too_close_warnings:
            warning_time = warning['time']
            # Find the envelope value at this time for positioning
            warning_envelope = np.interp(warning_time, time_axis, envelope_array)
            
            # Add a small, non-intrusive annotation
            fig.add_annotation(
                x=warning_time,
                y=warning_envelope,
                text=f"⚠ Too close ({warning['interval']:.3f}s < {warning['threshold']:.3f}s)",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=1,
                arrowcolor="orange",
                ax=0,
                ay=-50,
                font=dict(color="orange", size=8),
                bgcolor="rgba(0,0,0,0.5)",
                bordercolor="orange",
                borderwidth=1,
                borderpad=2
            )
    
    if group_stats:
        group_centers = []
        group_hover_texts = []
        
        for stat in group_stats:
            center_time = (stat['start_time'] + stat['end_time']) / 2
            center_envelope = np.interp(center_time, time_axis, envelope_array)
            group_centers.append((center_time, center_envelope))
            
            hover_text = f"Group {stat['group_id']}<br>"
            hover_text += f"S1-S2 Interval: {stat['avg_delta_t']:.3f}s<br>"
            if stat.get('avg_s2_s1_delta_t') is not None:
                hover_text += f"S2-S1 Interval: {stat['avg_s2_s1_delta_t']:.3f}s<br>"
            hover_text += f"BPM: {stat['avg_bpm']:.1f}<br>"
            hover_text += f"Range: {stat['start_time']:.1f}s - {stat['end_time']:.1f}s<br>"
            hover_text += f"S1 peaks: {stat['s1_count']}, S1-S2 pairs: {stat['pairs_count']}"
            if stat.get('s2_s1_pairs_count', 0) > 0:
                hover_text += f", S2-S1 pairs: {stat['s2_s1_pairs_count']}"
            group_hover_texts.append(hover_text)

            fig.add_annotation(
                x=center_time,
                y=center_envelope,
                text=f"{stat['avg_delta_t']:.3f}",
                showarrow=False,
                yshift=35, # Shift text above the center point
                font=dict(color="cyan", size=10),
                borderpad=4
            )
        
        if group_centers:
            center_times, center_envelopes = zip(*group_centers)
            fig.add_trace(go.Scatter(
                x=center_times,
                y=center_envelopes,
                mode="markers",
                name="Group Centers",
                marker=dict(size=10, color="rgba(0,0,0,0.1)"),
                customdata=group_hover_texts,
                hovertemplate="%{customdata}<extra></extra>",
                showlegend=False
            ))
    
    robust_upper_limit = np.quantile(envelope_array, 0.95) if len(envelope_array) > 0 else 1
    layout_config = {
        "template": "plotly_dark",
        "title_text": f"Heartbeat Analysis - {selected_file}",
        "dragmode": 'pan',
        "legend": dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        "margin": dict(t=140, b=100),
        "hovermode": 'x unified',
        "yaxis": dict(title="Signal Amplitude", range=[0, robust_upper_limit * 100.0]),
        "yaxis2": dict(title="BPM", overlaying="y", side="right", range=[50, 200], titlefont=dict(color="#4a4a4a"), tickfont=dict(color="#4a4a4a"))
    }
    
    layout_config["uirevision"] = selected_file
    
    fig.update_layout(**layout_config)
    
    if len(time_axis) > 0:
        tick_positions_sec = np.linspace(0, time_axis[-1], num=10)
        ticktext = [f"{int(s // 60):02d}:{int(s % 60):02d}" for s in tick_positions_sec]
        
        fig.update_xaxes(title_text="Time (seconds)", tickvals=tick_positions_sec, ticktext=ticktext, hoverformat='.2f')
    
    return fig, df.to_dict("records"), html.Ul([html.Li(i) for i in intervals]), undo_history

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
    
    df = pd.DataFrame(table_data) if table_data else pd.DataFrame(columns=["Time (s)", "Average BPM", "Peak Type"])
    
    if df.empty:
        return html.P("No data available for calculation.", style={"color": "red"})
    
    avg_delta_t, avg_bpm, pairs_in_range = calculate_avg_delta_t_in_range(df, start_time, end_time)
    if avg_delta_t is None:
        return html.P(f"No S1-S2 pairs found in time range {start_time:.3f}s to {end_time:.3f}s", style={"color": "orange"})
    
    pairs_text = [f"• S1 at {s1_time:.3f}s (BPM: {s1_bpm:.1f}) → S2 at {s2_time:.3f}s, S1-S2 Interval = {delta_t:.3f}s" for s1_time, s2_time, delta_t, s1_bpm in pairs_in_range]
    
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
    if not table_data:
        return html.P("No data available for group analysis.", style={"color": "gray"})
    
    df = pd.DataFrame(table_data)
    
    if df.empty:
        return html.P("No data available for group analysis.", style={"color": "gray"})
    
    groups = detect_labeling_groups(df, gap_threshold=5.0)
    
    if not groups:
        return html.P("No groups detected (need at least 2 S1 peaks with <5s gaps).", style={"color": "orange"})
    
    group_stats = calculate_group_statistics(df, groups)
    
    if not group_stats:
        return html.P("No valid groups found for analysis.", style={"color": "orange"})
    
    group_outputs = []
    for stat in group_stats:
        title_text = f"Group {stat['group_id']}: Average S1-S2 Interval: {stat['avg_delta_t']:.3f}s"
        if stat.get('avg_s2_s1_delta_t') is not None:
            title_text += f", Average S2-S1 Interval: {stat['avg_s2_s1_delta_t']:.3f}s"
        title_text += f", Average BPM: {stat['avg_bpm']:.1f}"
        
        pairs_text = f"S1 peaks: {stat['s1_count']}, S1-S2 pairs: {stat['pairs_count']}"
        if stat.get('s2_s1_pairs_count', 0) > 0:
            pairs_text += f", S2-S1 pairs: {stat['s2_s1_pairs_count']}"
        
        group_outputs.append(html.Div([
            html.H3(title_text, 
                   style={"fontSize": "20px", "fontWeight": "bold", "color": "#42bcf5", "marginBottom": "5px"}),
            html.P(f"Time range: {stat['start_time']:.3f}s - {stat['end_time']:.3f}s (Duration: {stat['duration']:.1f}s)", 
                  style={"fontSize": "12px", "marginBottom": "2px"}),
            html.P(pairs_text, 
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
