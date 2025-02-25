import os
import sys
from pathlib import Path
import logging 


while True :
    project_name = input("Enter your project Name : ")

    if project_name != "":
        print("Into break")
        break

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/utils/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "logs.py",
    "exception.py",
    "setup.py",
    ]

for file_path in list_of_files:
    print("into for loop")
    file_path = Path (file_path)
    filedir , filename = os.path.split(file_path)

    if filedir != "":
        os.mkdir(filedir)
        
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path , "w") as f:
            pass
    else: 
     print("into else")
    logging.info("File is already present at : {file_path}")
