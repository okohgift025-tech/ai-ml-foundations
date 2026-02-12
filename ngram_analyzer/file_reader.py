"""File ingestion module.

This module handles reading multiple text files and error handling.
"""

import os
from typing import List, Dict
from pathlib import Path


class FileIngestionError(Exception):
    """Custom exception for file ingestion errors."""
    pass


def read_file(file_path: str, encoding: str = 'utf-8') -> str:
    """Read a single text file.
    
    Args:
        file_path: Path to the file
        encoding: File encoding
        
    Returns:
        File contents as string
        
    Raises:
        FileIngestionError: If file cannot be read
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        raise FileIngestionError(f"File not found: {file_path}")
    except PermissionError:
        raise FileIngestionError(f"Permission denied: {file_path}")
    except UnicodeDecodeError:
        raise FileIngestionError(f"Encoding error in file: {file_path}")
    except Exception as e:
        raise FileIngestionError(f"Error reading file {file_path}: {str(e)}")


def read_multiple_files(file_paths: List[str], encoding: str = 'utf-8') -> Dict[str, str]:
    """Read multiple text files.
    
    Args:
        file_paths: List of file paths
        encoding: File encoding
        
    Returns:
        Dictionary mapping file paths to their contents
    """
    contents = {}
    errors = []
    
    for file_path in file_paths:
        try:
            contents[file_path] = read_file(file_path, encoding)
        except FileIngestionError as e:
            errors.append(str(e))
    
    if errors:
        print(f"Warning: {len(errors)} file(s) could not be read:")
        for error in errors:
            print(f"  - {error}")
    
    return contents


def read_directory(directory_path: str, pattern: str = "*.txt", 
                   encoding: str = 'utf-8') -> Dict[str, str]:
    """Read all files in a directory matching a pattern.
    
    Args:
        directory_path: Path to the directory
        pattern: File pattern to match (e.g., "*.txt")
        encoding: File encoding
        
    Returns:
        Dictionary mapping file paths to their contents
        
    Raises:
        FileIngestionError: If directory doesn't exist or is not accessible
    """
    try:
        dir_path = Path(directory_path)
        if not dir_path.exists():
            raise FileIngestionError(f"Directory not found: {directory_path}")
        
        if not dir_path.is_dir():
            raise FileIngestionError(f"Not a directory: {directory_path}")
        
        file_paths = [str(f) for f in dir_path.glob(pattern)]
        
        if not file_paths:
            print(f"Warning: No files matching '{pattern}' found in {directory_path}")
            return {}
        
        return read_multiple_files(file_paths, encoding)
        
    except FileIngestionError:
        raise
    except Exception as e:
        raise FileIngestionError(f"Error reading directory {directory_path}: {str(e)}")


def combine_file_contents(contents: Dict[str, str], separator: str = "\n\n") -> str:
    """Combine multiple file contents into a single string.
    
    Args:
        contents: Dictionary mapping file paths to contents
        separator: Separator to use between files
        
    Returns:
        Combined text string
    """
    return separator.join(contents.values())
