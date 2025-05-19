#!/usr/bin/env python
"""
Startup script for the FastAPI application.
"""
import subprocess
import sys
from pathlib import Path

def main():
    """Run development server with auto-reload."""
    # Get the project root directory
    project_dir = Path(__file__).parent
    
    # Settings for the server
    host = "localhost"
    port = 8000
    
    print("\nStarting FastAPI development server...")
    print("Access the application at http://localhost:8000\n")
    print("This will automatically manage dependencies as needed.\n")
    
    # Use uvicorn directly
    try:
        subprocess.run(
            [
                sys.executable, 
                "-m", 
                "uvicorn", 
                "app.main:app", 
                "--host", 
                host, 
                "--port", 
                str(port), 
                "--reload"
            ], 
            check=True
        )
    except KeyboardInterrupt:
        print("\nServer shutdown requested. Exiting...")
    except Exception as e:
        print(f"\nError starting server: {e}")

if __name__ == "__main__":
    main()
