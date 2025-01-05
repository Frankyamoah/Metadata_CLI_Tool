import click # Importing click for CLI functionality
import os # For file path operations
import subprocess # To run ExifTool commands

# Function to view metadata of a file
def view_metadata(image_path):
    """
    View metadata of an image file
    """
    try:
        result = subprocess.run(
            ["exiftool", image_path], capture_output=True, text=True
        )
        click.echo(result.stdout)
    except Exception as e: 
        click.echo(f"Error viewing metadata: {e}")