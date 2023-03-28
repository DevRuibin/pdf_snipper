from sys import exit

import argparse
import os
from PyPDF2 import PdfWriter, PdfReader
from termcolor import colored

from pdf_snipper.snipper_error.handler import Handler
from pdf_snipper.snipper_utils.tool import Tool



class PdfMerge(Tool):
    def __init__(self, args):
        super().__init__()
        self.start_page = args.start_page
        self.end_page = args.end_page
        self.pdf_file = args.pdf_file
        self.output_file = args.output_file

    def run(self):
        # check if input file exists
        if self.pdf_file and not os.path.exists(self.pdf_file):
            print(colored(f"ERROR: File {self.pdf_file} does not exist.", 'red'))
            exit(1)

        # check for missing or invalid arguments
        try:
            if not self.pdf_file:
                raise argparse.ArgumentError(None, "Missing required argument: -i/--input")
            elif not self.start_page and not self.end_page:
                raise argparse.ArgumentError(None, "At least one of -s/--start_page and -e/--end_page must be provided")
            elif self.start_page and self.end_page and self.start_page > self.end_page:
                raise argparse.ArgumentError(None, "Start page cannot be greater than end page")
        except argparse.ArgumentError as e:
            print(colored(f"ERROR: {e}", 'red'))
            exit(1)

        # read input PDF file
        pdf_file = PdfReader(open(self.pdf_file, "rb"))
        pdf_pages_len = len(pdf_file.pages)

        # set start and end page numbers
        start_page = self.start_page or 1
        end_page = self.end_page or pdf_pages_len

        # check start and end page numbers
        if start_page < 1:
            start_page = 1
            Handler.handle_warning("WARNING: Start page cannot be less than 1. Setting start page to 1.")
        if start_page > pdf_pages_len:
            start_page = 1
            Handler.handle_warning("WARNING: Start page cannot be greater than the number of pages in the PDF file. "
                                   "Setting start page to 1.")
        if end_page > pdf_pages_len:
            end_page = pdf_pages_len
            Handler.handle_warning("WARNING: End page cannot be greater than the number of pages in the PDF file. "
                                   "Setting end page to {}.".format(pdf_pages_len))
        if start_page > end_page:
            start_page, end_page = end_page, start_page
            Handler.handle_warning("WARNING: Start page cannot be greater than end page. Swapping start and end pages.")

        # create PdfWriter object
        output = PdfWriter()

        # add pages to PdfWriter object
        for i in range(start_page - 1, end_page):
            output.add_page(pdf_file.pages[i])

        # set output file path
        pdf_name, pdf_ext = os.path.splitext(os.path.basename(self.pdf_file))
        output_file = self.output_file or "{}_{}-{}{}".format(pdf_name, start_page, end_page, pdf_ext)

        # check if output file exists
        if os.path.exists(output_file):
            Handler.handle_warning("WARNING: Output file already exists. Do you want to overwrite it? (y/n) ")
            overwrite = input()
            if overwrite.lower != 'y':
                Handler.handle_error("Aborting. No changes were made.")

        # write output file
        with open(output_file, "wb") as outputStream:
            output.write(outputStream)
            Handler.handle_info("Output file saved to {}".format(output_file))
