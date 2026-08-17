import os
from pathlib import Path

print("Current Directory:", os.getcwd())
print("Files and Folders:", os.listdir())

folder_name = "Purva"
os.makedirs(folder_name, exist_ok=True)

path = Path(folder_name)
path.mkdir(parents=True, exist_ok=True)

print("Folder created successfully.")
