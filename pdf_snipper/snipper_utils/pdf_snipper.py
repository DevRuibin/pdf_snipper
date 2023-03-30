from sys import exit

import argparse
import os
from PyPDF2 import PdfWriter, PdfReader
from termcolor import colored

from pdf_snipper import utils
from pdf_snipper.snipper_error.handler import Handler
from pdf_snipper.snipper_utils.tool import Tool


class PdfSnipper(Tool):
    def __init__(self, args):
        super().__init__()
        self.start_page = args.start_page
        self.end_page = args.end_page
        self.pages = args.pages
        self.pdf_file = args.pdf_file
        self.output_file = args.output_file
        self.check_args()

    def extract_pages(self, pdf_name, pdf_ext, pdf_file, pdf_pages_len, output):
        for page_num in self.pages:
            if page_num < 1 or page_num > pdf_pages_len:
                Handler.handle_warning(f"WARNING: Page number {page_num} is out of range. Skipping...")
            else:
                output.add_page(pdf_file.pages[page_num - 1])
        return self.output_file or "{}_{}{}".format(pdf_name, "snipper", pdf_ext)

    def snipper(self, pdf_file, pdf_pages_len, output, pdf_name, pdf_ext):

        # set start and end page numbers
        start_page = self.start_page or 1
        end_page = self.end_page or pdf_pages_len

        # check start and end page numbers
        if start_page < 1:
            start_page = 1
            Handler.handle_warning("WARNING: Start page cannot be less than 1. Setting start page to 1.")
        if start_page > pdf_pages_len:
            start_page = 1
            Handler.handle_warning("WARNING: Start page cannot be greater than the number of pages in the PDF file."
                                   "Setting start page to 1.")
        if end_page > pdf_pages_len:
            end_page = pdf_pages_len
            Handler.handle_warning("WARNING: End page cannot be greater than the number of pages in the PDF file. "
                                   "Setting end page to {}.".format(pdf_pages_len))
        if start_page > end_page:
            start_page, end_page = end_page, start_page
            Handler.handle_warning("WARNING: Start page cannot be greater than end page. Swapping start and end "
                                   "pages.")
        for i in range(start_page - 1, end_page):
            output.add_page(pdf_file.pages[i])
        return self.output_file or "{}_{}-{}{}".format(pdf_name, start_page, end_page, pdf_ext)

    def check_args(self):
        # check if input file exists
        if self.pdf_file and not os.path.exists(self.pdf_file):
            Handler.handle_error(f"ERROR: File {self.pdf_file} does not exist.")

        # check for missing or invalid arguments
        if not self.pdf_file:
            Handler.handle_error("Missing required argument: -i/--input")
        elif not self.pages and (not self.start_page and not self.end_page):
            Handler.handle_error("At least one of -p/--pages or -s/--start_page and -e/--end_page "
                                 "must be provided")
        elif self.start_page and self.end_page and self.start_page > self.end_page:
            Handler.handle_error("Start page cannot be greater than end page")

    def run(self):

        # read input PDF file
        pdf_file = PdfReader(open(self.pdf_file, "rb"))
        pdf_pages_len = len(pdf_file.pages)

        # create PdfWriter object
        output = PdfWriter()
        pdf_name, pdf_ext = os.path.splitext(os.path.basename(self.pdf_file))

        # add pages to PdfWriter object
        if self.pages:
            output_file = self.extract_pages(pdf_name, pdf_ext, pdf_file, pdf_pages_len, output)
            for page_num in self.pages:
                if page_num < 1 or page_num > pdf_pages_len:
                    Handler.handle_warning(f"WARNING: Page number {page_num} is out of range. Skipping...")
                else:
                    output.add_page(pdf_file.pages[page_num - 1])
        else:
            output_file = self.snipper(pdf_file, pdf_pages_len, output, pdf_name, pdf_ext)

        # write output file
        utils.check_output_file_and_write_output_file(output_file, output)
