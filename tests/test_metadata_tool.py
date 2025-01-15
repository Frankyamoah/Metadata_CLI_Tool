import os
import pytest
from metadata_tool import view_metadata, add_metadata, remove_metadata, cli
from click.testing import CliRunner

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


# Test the CLI for adding metadata
def test_cli_add_metadata(sample_image,mocker):
    """
    Testing the cli command for adding metadata to an image file 
    
    Args:
    sample_image(str): Path to the temporary image file
    mocker(pytest fixture): A mocker object that can be used to mock the subprocess.run function

    """
    # Mock subprocess.run to avoid executing the actual ExifTool command
    mock_subprocess = mocker.patch("subprocess.run")

    # Create an instance of CliRunner for testing the CLI
    runner = CliRunner()

    # Invoke the CLI command with metadata
    result = runner.invoke(cli, ["add-metadata", os.path.abspath(sample_image), "--metadata", "Author=John Doe"])

    # Ensure the CLI command ran successfully
    assert result.exit_code == 0
    assert "Added metadata: Author=John Doe" in result.output

    # Verify that subprocess.run was called with the correct arguments
    mock_subprocess.assert_any_call(
        ["exiftool", "-Author=John Doe", os.path.abspath(sample_image)],
        capture_output=True,
    )


# Test the CLI for viewing metadata
def test_cli_view_metadata(sample_image, mocker):
    """
    Testing the cli command for viewing metadata of an image file 
    
    Args:
    sample_image(str): Path to the temporary image file
    mocker(pytest fixture): A mocker object that can be used to mock the subprocess.run function

    """
    # Mock subprocess.run to avoid executing the actual ExifTool command
    mock_subprocess = mocker.patch("subprocess.run")

    # Define mock return value for subprocess.run
    mock_subprocess.return_value.stdout = "Author: John Doe\nCopyright: Frank Yamoah\n"

    # Create an instance of CliRunner for testing the CLI
    runner = CliRunner()

    # Invoke the CLI command to view metadata
    result = runner.invoke(cli, ["view-metadata", os.path.abspath(sample_image)])

    # Ensure the CLI command ran successfully
    assert result.exit_code == 0
    assert "Author: John Doe" in result.output
    assert "Copyright: Frank Yamoah" in result.output

    # Verify that subprocess.run was called with the correct arguments
    mock_subprocess.assert_called_once_with(
        ["exiftool", os.path.abspath(sample_image)],
        capture_output=True,
        text=True,
    )


# Test the CLI for removing metadata
def test_cli_remove_metadata(sample_image, mocker):
    """
    Test the CLI command for removing metadata from an image file.

    Args:
        sample_image (str): Path to the temporary image file.
        mocker (pytest fixture): A mocker object to mock subprocess.run.
    """
    # Mock subprocess.run to avoid executing the actual ExifTool command
    mock_subprocess = mocker.patch("subprocess.run")

    # Create an instance of CliRunner for testing the CLI
    runner = CliRunner()

    # Invoke the CLI command to remove metadata
    result = runner.invoke(cli, ["remove-metadata", os.path.abspath(sample_image), "--keys", "Author"])

    # Ensure the CLI command ran successfully
    assert result.exit_code == 0
    assert "Removed metadata: Author" in result.output

    # Verify that subprocess.run was called with the correct arguments
    mock_subprocess.assert_called_once_with(
        ["exiftool", "-Author=", os.path.abspath(sample_image)],
        capture_output=True,
    )
