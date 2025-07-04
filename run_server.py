#!/usr/bin/env python3
"""
Startup script for the BPM Analysis Web Application
"""

import os
import sys
import subprocess

def main():
    """Start the Django development server"""
    print("BPM Analysis Web Application")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("Error: manage.py not found. Please run this script from the Django project directory.")
        sys.exit(1)
    
    # Check if migrations are up to date
    try:
        print("Checking Django setup...")
        result = subprocess.run([sys.executable, 'manage.py', 'check'], 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print("Django check failed:")
            print(result.stderr)
            sys.exit(1)
        print("✓ Django setup OK")
    except Exception as e:
        print(f"Error running Django check: {e}")
        sys.exit(1)
    
    # Start the server
    try:
        print("\nStarting Django development server...")
        print("The application will be available at: http://localhost:8000")
        print("Press Ctrl+C to stop the server")
        print("-" * 40)
        
        subprocess.run([sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'])
        
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()