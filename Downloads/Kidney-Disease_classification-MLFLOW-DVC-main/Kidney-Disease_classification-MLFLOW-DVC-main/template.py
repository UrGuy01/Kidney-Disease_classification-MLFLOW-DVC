import os
from pathlib import Path
import logging

#logging string...
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s] :%(message)s:')

project_name = 'CnnClassifier'

from pathlib import Path

project_name = "my_project"  # Replace with your actual project name

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

for file_path in list_of_files:
    path = Path(file_path)
    directory, filename = path.parent, path.name

    print(f"Directory: {directory}")
    print(f"File Name: {filename}")
    
    
    if directory != "":
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Creating directory: {directory} for the file: {filename}")

    # Create an empty file if it doesn't exist or is empty
    if (not path.exists()) or (path.stat().st_size == 0):
        with open(path, "w") as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")