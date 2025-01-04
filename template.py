import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project name
project_name = 'Kidney Disease Classification'

# List of files to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Iterate through the list of files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath)  # Split directory and file name

    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Create the directory structure
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # Create empty files if they don't exist or are empty
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            pass  # Create an empty file
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

