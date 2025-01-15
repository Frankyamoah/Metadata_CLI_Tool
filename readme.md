# Image Metadata CLI Tool

A command-line interface tool for managing image metadata using ExifTool. This tool allows you to view, add, remove, and manage metadata for image files.

## Features

- View existing metadata of image files
- Add new metadata to images
- Remove specific metadata fields
- Replace existing metadata
- Handle multiple images at once
- Verify metadata in images

## Requirements

- Python 3.11 or higher
- ExifTool (must be installed on your system)
- Click library (Python package)

## Installation

1. First, ensure ExifTool is installed on your system:
   - For macOS: `brew install exiftool`
   - For Ubuntu/Debian: `sudo apt-get install libimage-exiftool-perl`
   - For Windows: Download from [ExifTool website](https://exiftool.org)

2. Clone this repository:
   ```bash
   git clone [your-repository-url]
   cd metadata-cli-tool
   ```

3. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Viewing Metadata

To view metadata of an image:
```bash
python metadata_tool.py view-metadata path/to/image.jpg
```

### Adding Metadata

To add metadata to an image:
```bash
python metadata_tool.py add-metadata path/to/image.jpg --metadata "Author=John Doe" --metadata "Copyright=© 2025"
```

You can add multiple metadata fields at once by using multiple `--metadata` options.

### Removing Metadata

To remove specific metadata fields:
```bash
python metadata_tool.py remove-metadata path/to/image.jpg --keys "Author" --keys "Copyright"
```

### Replacing Metadata

To replace existing metadata:
```bash
python metadata_tool.py replace-metadata path/to/image.jpg --metadata "Author=New Author"
```

### Verifying Metadata

To verify metadata in an image:
```bash
python metadata_tool.py verify-metadata path/to/image.jpg
```

### Working with Multiple Files

All commands support multiple image files:
```bash
python metadata_tool.py add-metadata image1.jpg image2.jpg --metadata "Author=John Doe"
```

## Default Metadata

The tool includes default metadata that will be applied when adding metadata:
- Author: Frank Yamoah
- Copyright: © 2025 Frank Yamoah. All rights reserved.

## Testing

To run the tests:
```bash
PYTHONPATH=. pytest -v
```

## Error Handling

The tool includes error handling for common issues:
- Missing ExifTool installation
- Invalid file paths
- Incorrect metadata format
- File access permissions


## Author

Frank Yamoah

## Acknowledgments

- ExifTool for providing the underlying metadata manipulation capabilities
- Click library for the CLI interface