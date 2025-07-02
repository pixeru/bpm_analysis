import ttkbootstrap as ttkb
from gui import BPMApp
import logging
import sys

def main():
    """
    Initializes and runs the BPM Analysis GUI.
    This is the main entry point for the application.
    """
    # Configure logging for the entire application
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(message)s',
        stream=sys.stdout
    )
    
    root = ttkb.Window(themename="minty")
    app = BPMApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
