# Mismatched File & Folder Finder

## Project Overview

A Streamlit web application that scans directory structures to identify folders containing files that don't follow a specific naming convention. The tool is designed to help maintain consistent file naming patterns across large directory structures.

## Purpose

This application identifies folders where files don't match the expected naming pattern:
- Expected pattern: `{folder_name}_{###}` (where ### is exactly 3 digits)
- Supported file types: `.jpg`, `.jpeg`, `.png`, `.eip`

## Technical Stack

- **Framework**: Streamlit
- **Language**: Python 3
- **Core Libraries**:
  - `streamlit` - Web interface
  - `os` - File system operations
  - `re` - Regular expression pattern matching

## Project Structure

```
mismatched-file-folder-finder/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # Project documentation
```

## Core Functionality

### `scan_directory(base_dir)`

Recursively walks through a directory tree and identifies mismatched files.

**Logic**:
1. Traverses all subdirectories starting from `base_dir`
2. For each folder, examines files with supported extensions
3. Checks if file base name matches: `{folder_name}_{3_digits}`
4. Returns a set of folder paths containing at least one mismatched file

**Example**:
- Folder: `vacation_photos`
- Valid files: `vacation_photos_001.jpg`, `vacation_photos_042.png`
- Invalid files: `vacation_photos.jpg`, `vacation_photos_1.jpg`, `photo_001.jpg`

### User Interface

The Streamlit app provides:
- Text input for directory path
- Scan button to trigger analysis
- Error handling for invalid paths
- Color-coded results (orange highlighting for mismatched folder names)
- Attribution footer with link to creator's website

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   streamlit run app.py
   ```

3. Enter a directory path in the web interface
4. Click "Scan Directory" to analyze
5. Review results showing folders with mismatched files

## Key Features

- Recursive directory scanning
- Pattern validation using regex
- Clean, user-friendly web interface
- Performance optimized (breaks on first mismatch per folder)
- Sorted output for easy reading
- Visual highlighting of problematic folders

## Use Cases

- Digital asset management
- Photo library organization
- Project file structure validation
- Quality assurance for file naming conventions
- Bulk file organization auditing

## File Naming Convention

The tool enforces this strict naming pattern:
```
{exact_folder_name}_{exactly_3_digits}.{extension}
```

Where:
- Folder name must match exactly (case-sensitive)
- Must have underscore separator
- Must have exactly 3 digits (000-999)
- Supported extensions: jpg, jpeg, png, eip

## Author

Created by Herman Jordaan Digi
Website: https://www.herman-jordaan.com/
