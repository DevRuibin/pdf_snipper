import os

from pdf_snipper.snipper_error.handler import Handler


def check_output_file(output_file):
    # check if output file exists
    if os.path.exists(output_file):
        Handler.handle_warning("WARNING: Output file already exists. Do you want to overwrite it? (y/n) ")
        overwrite = input()
        if overwrite.lower() != 'y':
            Handler.handle_error("Aborting. No changes were made.")


def write_output_file(output, output_file):
    # write output file
    with open(output_file, "wb") as outputStream:
        output.write(outputStream)
        Handler.handle_info("Output file saved to {}".format(output_file))


def check_output_file_and_write_output_file(output, output_file):
    check_output_file(output_file)
    write_output_file(output, output_file)