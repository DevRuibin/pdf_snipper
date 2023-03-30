import os

from PyPDF2 import PdfMerger

from pdf_snipper import utils
from pdf_snipper.snipper_error.handler import Handler
from pdf_snipper.snipper_utils.tool import Tool


class PdfMerge(Tool):
    def __init__(self, args):
        super().__init__()
        self.pdf_files = args.pdf_files
        self.output_file = args.output_file

    def run(self):
        # check if input files exist
        for pdf_file in self.pdf_files:
            if not os.path.exists(pdf_file):
                Handler.handle_error(f"ERROR: File {pdf_file} does not exist.")

        # check for missing or invalid arguments
        if not self.pdf_files:
            Handler.handle_error("Missing required argument: -i/--input")

        # create PdfFileMerger object
        merger = PdfMerger()

        # add pages to PdfFileMerger object
        for pdf_file in self.pdf_files:
            with open(pdf_file, "rb") as pdf:
                merger.append(pdf)

        # set output file path
        output_file = self.output_file or "{}_merged.pdf".format(os.path.splitext(os.path.basename(self.pdf_files[0]))[0])

        utils.check_output_file(output_file)

        # write output file
        with open(output_file, "wb") as output:
            merger.write(output)
            Handler.handle_info("Output file saved to {}".format(output_file))
