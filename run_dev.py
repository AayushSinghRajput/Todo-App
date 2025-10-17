# Import necessary modules
import subprocess  # To run Flask app as a separate process
import time        # To pause the script in a loop
from watchdog.observers import Observer           # Observer monitors file system changes
from watchdog.events import FileSystemEventHandler  # Handles events when files change

# Define a class to handle file changes and restart the Flask app
class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        # Keep track of the currently running Flask process
        self.process = None
        # Start the Flask app immediately when the watcher starts
        self.run_app()

    # Method to start or restart the Flask app
    def run_app(self):
        # If a Flask process is already running, terminate it
        if self.process:
            self.process.terminate()
        
        # Print a log message for clarity
        print("\n🚀 Starting Flask app...\n")
        
        # Start a new process to run the Flask app (app.py)
        # subprocess.Popen allows the process to run in the background
        self.process = subprocess.Popen(["python", "app.py"])

    # Method called automatically whenever any file changes
    def on_any_event(self, event):
        # Check if the changed file is a Python file
        if event.src_path.endswith(".py"):
            # Print which file changed
            print(f"\n🔁 File changed: {event.src_path}")
            # Restart the Flask app
            self.run_app()

# Main part of the script
if __name__ == "__main__":
    # Create an instance of the ReloadHandler
    event_handler = ReloadHandler()
    
    # Create an Observer that will watch the file system
    observer = Observer()
    
    # Schedule the observer to monitor the current directory (".") recursively
    # recursive=True means it will watch all subfolders as well
    observer.schedule(event_handler, ".", recursive=True)
    
    # Start the observer
    observer.start()
    
    # Print a log message to indicate the watcher is active
    print("👀 Watching for file changes...")

    # Keep the script running indefinitely so the observer can keep monitoring
    try:
        while True:
            time.sleep(1)  # Sleep 1 second per loop to reduce CPU usage
    except KeyboardInterrupt:
        # Stop the observer gracefully if user presses Ctrl+C
        observer.stop()
    
    # Wait until the observer thread finishes before exiting
    observer.join()
