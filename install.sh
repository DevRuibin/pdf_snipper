#!/bin/bash


# Navigate to the directory containing the shell script
cd /path/to/directory

# Install PyInstaller
pip install pyinstaller

# Install the dependencies
pip install -r requirements.txt

pyinstaller pdf_snipper/__main__.py --name snipper --onefile

# Navigate to the dist directory
cd dist

# Run the executable
./snipper

