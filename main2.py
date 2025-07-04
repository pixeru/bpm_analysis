import os
import sys
import logging
from bpm_analysis import analyze_wav_file, convert_to_wav
from config import DEFAULT_PARAMS
import shutil

def main():
    """
    Runs BPM analysis on sample_input.wav without GUI.
    This is a command-line version of the BPM analyzer.
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(message)s',
        stream=sys.stdout
    )
    
    # FILE PATH GOES HERE - Edit this path to point to your sample_input.wav file
    sample_file_path = os.path.join("samples", "sample_input.wav")
    
    # Check if the sample file exists
    if not os.path.exists(sample_file_path):
        logging.error(f"Sample file not found at: {sample_file_path}")
        logging.error("Please ensure the file exists or update the path in main2.py")
        return
    
    # Create output directory
    output_dir = os.path.join(os.getcwd(), "processed_files")
    os.makedirs(output_dir, exist_ok=True)
    
    # Analysis parameters (using defaults from config)
    params = DEFAULT_PARAMS.copy()
    
    # Optional: Set a starting BPM hint (set to None to auto-detect)
    start_bpm_hint = None  # You can set this to a specific value like 80.0 if needed
    
    try:
        logging.info(f"Starting analysis of: {sample_file_path}")
        
        # Determine the WAV file path for processing
        base_name, ext = os.path.splitext(sample_file_path)
        wav_path = os.path.join(output_dir, f"{os.path.basename(base_name)}.wav")
        
        # Convert to WAV if needed
        if ext.lower() != '.wav':
            logging.info(f"Converting {os.path.basename(sample_file_path)} to WAV format...")
            if not convert_to_wav(sample_file_path, wav_path):
                raise Exception("File conversion failed.")
        else:
            # Copy WAV file to output directory
            shutil.copy(sample_file_path, wav_path)
        
        logging.info("Starting heartbeat analysis...")
        
        # Run the analysis
        analyze_wav_file(
            wav_path, 
            params, 
            start_bpm_hint, 
            original_file_path=sample_file_path,
            output_directory=output_dir
        )
        
        logging.info("Analysis completed successfully!")
        logging.info(f"Results saved to: {output_dir}")
        
    except Exception as e:
        logging.error(f"Analysis failed: {str(e)}")
        return

if __name__ == "__main__":
    main() 