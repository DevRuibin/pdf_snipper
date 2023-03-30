import os

from pdf_snipper.snipper_error.handler import Handler


def check_output_file(output_file):
    # check if output file exists
    if os.path.exists(output_file):
        Handler.handle_warning("WARNING: Output file already exists. Do you want to overwrite it? (y/n) ")
        overwrite = input()
        if overwrite.lower() != 'y':
            Handler.handle_error("Aborting. No changes were made.")