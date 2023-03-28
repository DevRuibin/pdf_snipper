#!/bin/bash

# Install PyInstaller
pip install pyinstaller

# Navigate to the directory containing the Python script
cd /path/to/directory

# Package the script and its dependencies into a standalone executable
pyinstaller --onefile pdf_snipper.py

# Create a symlink to the executable file in /usr/local/bin
sudo ln -s $(pwd)/dist/pdf_snipper /usr/local/bin/pdf_snipper
