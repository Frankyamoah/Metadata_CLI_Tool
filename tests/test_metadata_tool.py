import os
import pytest
from metadata_tool import view_metadata, add_metadata, remove_metadata, cli

@pytest.fixture
def sample_image(temp_path):
    """
    Creating temporary image for testing purposes

    """
    # Define the path for temporary image file
    image_path = temp_path / "test_image.jpg"

    #Open the file in write-binary mode ("wb")
    with open(image_path, "wb") as f:
        # Write dummy binary data to the file
        f.write(b"Test Image Data")

    # Return the path to the temporary image file
    return str(image_path)

def test_add_metadata(sample_image, mocker):
    """
    Test the add metadata function

    """

    # Mock the subprocess.run to avoid calling the ExifTool
    mock_subprocess_run = mocker.patch("subprocess.run")

    # Call the add metadata function
    add_metadata(["test_image.jpg"], ["Author=John Doe"])