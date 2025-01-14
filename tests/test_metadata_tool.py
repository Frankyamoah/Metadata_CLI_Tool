import pytest
from metadata_tool import view_metadata, add_metadata, remove_metadata, cli

@pytest.fixture

# Create a temporary image file for testing
def sample_image(tmp_path):
    """
    Creating temporary image for testing purposes
    Args:
    tmp_path: pytest fixture that provides a temporary directory path
    Returns:
    str: Path to the temporary image file

    """
    # Define the path for temporary image file
    image_path = tmp_path / "test_image.jpg"

    #Open the file in write-binary mode ("wb")
    with open(image_path, "wb") as f:
        # Write dummy binary data to the file
        f.write(b"Test Image Data")

    # Return the path to the temporary image file
    return str(image_path)

# Test the add_metadata function
def test_add_metadata(sample_image, mocker):
    """
    Test the add metadata function to ensure it calls the subprocess.run with the correct arguments

    Args:
    sample_image (str): Path to the temporary image file
    mocker(pytest fixture): A mocker object that can be used to mock the subprocess.run function

    """

    # Mock the subprocess.run to avoid calling the ExifTool
    mock_subprocess = mocker.patch("subprocess.run")

    # Call the add metadata function
    add_metadata(["sample_image"], ["Author=John Doe"])

    # Assert that the subprocess.run was called with the correct arguments
    assert mock_subprocess.call_count == 1

    # Check the exact command used in the subprocess.run call
    mock_subprocess.assert_called_with(
        ["exiftool", "-Author=John Doe", sample_image],
        capture_output=True,
    )

# Test the remove_metadata function
def test_remove_metadata(sample_image, mocker):
    """
    Test the remove metadata function to ensure it calls the subprocess.run with the correct arguments

    Args:
    sample_image (str): Path to the temporary image file
    mocker(pytest fixture): A mocker object that can be used to mock the subprocess.run function

    """

    # Mock the subprocess.run to avoid calling the ExifTool
    mock_subprocess = mocker.patch("subprocess.run")

    # Call the remove metadata function
    remove_metadata(["sample_image"], ["Author"])

    # Assert that the subprocess.run was called with the correct arguments
    assert mock_subprocess.call_count == 1

    # Check the exact command used in the subprocess.run call
    mock_subprocess.assert_called_with(
        ["exiftool", "-Author=", sample_image],
        capture_output=True,
    )

# Test the view_metadata function

def test_view_metadata(sample_image, mocker):
    """
    Test the view_metadata function to ensure it calls subprocess.run correctly.

    Args:
        sample_image (str): The path to the temporary image file.
        mocker (pytest fixture): A mocker object for patching.
    """
    # Mock subprocess.run
    mock_subprocess = mocker.patch("subprocess.run")

    # Define mock return value for subprocess.run
    mock_subprocess.return_value.stdout = "Author: John Doe\nCopyright: Frank Yamoah\n"

    # Call the function under test
    view_metadata(sample_image)

    # Verify subprocess.run was called once
    mock_subprocess.assert_called_once_with(
        ["exiftool", sample_image],
        capture_output=True,
        text=True,
    )