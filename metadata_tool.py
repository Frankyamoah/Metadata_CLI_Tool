import click # Importing click for CLI functionality
import subprocess # To run ExifTool commands

DEFAULT_METADATA = {
    "Author": "Frank Yamoah",
    "Copyright": "© 2025 Frank Yamoah. All rights reserved.",
}

@click.group()
def cli():
    """
    CLI tool for managing image metadata using ExifTool
    """

# Function to view metadata of a file
@cli.command()
@click.argument("image_paths", nargs=-1, type=click.Path(exists=True))
def view_metadata(image_paths):
    """
    View metadata of an image file

    Args: 
    image_path (tuple): This provides the path to the image file that needs its metadata viewed
    
    This function uses the 'subprocess' module to invoke the ExifTool command line tool
    to extract and display the metadata of the specified image file. This then prints the extracted
    metadata to the console.
    """
    for image_path in image_paths:  # Add loop to handle multiple files
        try:
        # Use subprocess.run to execute the ExifTool command-line tool
            result = subprocess.run(
                ["exiftool", image_path],       # Command to execute the ExifTool tool with the image path as an arguement
                capture_output=True,            # Capture both stdout and stderr to process the output
                text=True                       # Return the output as a string
        )
        # Print the metadata to the console
            click.echo(result.stdout)
        except Exception as e: 
        # If an exception occurs (e.g. Exif tool not installed or the file doesnt exist), handle the error
            click.echo(f"Error viewing metadata: {e}") # Print the error message to the console

# Functionto to add metadata to a file
@cli.command()
@click.argument("image_paths", nargs=-1, type=click.Path(exists=True)) # Arguements for the command line, image path, multiple values allowed, must be a valid path
@click.option(
    "--metadata",
    multiple=True,
    help="Metadata to add in the format of KEY=VALUE, e.g. 'Author=John Doe', Use multiple times to add more fields)",
)
def add_metadata(image_paths, metadata):
    """
    Add metadata to an image. Formate: KEY=VALUE.
    
    Args:
    image_path (tuple): This provides the path to the image file
    metadata(str): This provides the metadata to be added to the image
    
    """

    #combined default metadata with user-provided metadata
    combined_metadata = {**DEFAULT_METADATA}
    
    for meta in metadata:
        try:
            #Split user-provided metadata into key-value pairs
            key, value = meta.split("=")
            combined_metadata[key] = value
        except ValueError:
            click.echo(f"Invalid metadata format: {meta}. Use KEY=VALUE format")    
            return

    for image_path in image_paths:
        try:
            # Add each metadata field to the image
            for key, value in combined_metadata.items():
                subprocess.run(
                    ["exiftool", f"-{key}={value}", image_path],
                    capture_output=True,
                )
                click.echo(f"Added metadata: {key}={value} to {image_path}")
        except Exception as e:
                click.echo(f"Error adding metadata to {image_path}: {e}")

# Function to remove metadata from a file
@cli.command()
@click.argument("image_paths", nargs=-1, type=click.Path(exists=True))
@click.option(
    "--keys",
    multiple=True,
    help="Metadata keys to delete. Use multiple options for more keys.",
)
def remove_metadata(image_paths, keys):
    """
    Remove metadata from an image file
    
    Args:
    image_path (tuple): Tuple of image paths providedas arguments
    keys (list): List of metadata keys to delete
    """

    for image_path in image_paths:
        try:
            # Remove each metadata field from the image
            for key in keys:
                subprocess.run(
                    ["exiftool", f"-{key}=", image_path],
                    capture_output=True,
                )
                click.echo(f"Removed metadata: {key} from {image_path}")
        except Exception as e:
            click.echo(f"Error removing metadata from {image_path}: {e}")

# Function to replace metadata in an image
@cli.command()
@click.argument("image_paths", nargs=-1, type=click.Path(exists=True))
@click.option(
    "--metadata",
    multiple=True,
    help="Metadata to replace in the format KEY=VALUE. Use multiple options for more fields.",
)
def replace_metadata(image_paths, metadata):
    """
    Replace metadata in an image
    
    Args: 
    image_path (tuple) = Tuple of image paths added as aguements
    metadata (list) = List of meetadata to replace in the format of Key-Value pairs

    """
    for image_path in image_paths:
        try:
            # Replace each corresponding metadata field in the image
            for meta in metadata:
                    key, value = meta.split("=")
                    subprocess.run(
                        ["exiftool", f"-{key}={value}", image_path],
                        capture_output=True,
                    )
                    click.echo(f"Replaced metadata: {key}={value} in {image_path}")
        except Exception as e:
                    # Handle invalid metadata format
                    click.echo(f"Invalid metadata format: {e}. Use KEY=VALUE format")

# Function to Verify/Check metaata in an image
@cli.command()
@click.argument("image_paths", nargs=-1, type=click.Path(exists=True))
@click.option(
    "--keys",
    multiple=True,
    help="Metadata keys to verify. Use multiple options for more keys.",
)

def verify_metadta(image_paths):
    """
    Verify the metadata of one or more images.

    Args:
    image_paths (tuple): Tuple of image paths provided as arguments.
    """
    for image_path in image_paths:
        try:
            # Run ExifTool to verify metadata
            result = subprocess.run(
                ["exiftool", image_path], capture_output=True, text=True
            )
            # Output the metadata to the console
            click.echo(f"Metadata for {image_path}:\n{result.stdout}")
        except Exception as e:
            # Handle errors for each image
            click.echo(f"Error verifying metadata for {image_path}: {e}")

if __name__ == "__main__":
    cli() # Run the CLI tool
                    