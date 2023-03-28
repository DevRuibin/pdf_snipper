from sys import exit

import argparse
import os
from PyPDF2 import PdfWriter, PdfReader
from termcolor import colored

# create argument parser
parser = argparse.ArgumentParser(description='Extract a range of pages from a PDF file. \n The start number of a pdf file is 1')
parser.add_argument('-s', '--start_page', type=int, help='Starting page number (inclusive)')
parser.add_argument('-e', '--end_page', type=int, help='Ending page number (inclusive)')
parser.add_argument('-i', '--input', dest='pdf_file', type=str, help='Path to the input PDF file')
parser.add_argument('-o', '--output', dest='output_file', type=str, help='Path to the output PDF file')
args, _ = parser.parse_known_args()

# check if input file exists
if args.pdf_file and not os.path.exists(args.pdf_file):
    print(colored(f"ERROR: File {args.pdf_file} does not exist.", 'red'))
    exit(1)

# check for missing or invalid arguments
try:
    if not args.pdf_file:
        raise argparse.ArgumentError(None, "Missing required argument: -i/--input")
    elif not args.start_page and not args.end_page:
        raise argparse.ArgumentError(None, "At least one of -s/--start_page and -e/--end_page must be provided")
    elif args.start_page and args.end_page and args.start_page > args.end_page:
        raise argparse.ArgumentError(None, "Start page cannot be greater than end page")
except argparse.ArgumentError as e:
    print(colored(f"ERROR: {e}", 'red'))
    exit(1)

# read input PDF file
pdf_file = PdfReader(open(args.pdf_file, "rb"))
pdf_pages_len = len(pdf_file.pages)

# set start and end page numbers
start_page = args.start_page or 1
end_page = args.end_page or pdf_pages_len

# check start and end page numbers
if start_page < 1:
    start_page = 1
    print(colored("WARNING: Start page cannot be less than 1. Setting start page to 1.", 'yellow'))
if start_page > pdf_pages_len:
    start_page = 1
    print(colored("WARNING: Start page cannot be greater than the number of pages in the PDF file. Setting start page to 1.", 'yellow'))
if end_page > pdf_pages_len:
    end_page = pdf_pages_len
    print(colored("WARNING: End page cannot be greater than the number of pages in the PDF file. Setting end page to {}.".format(pdf_pages_len), 'yellow'))
if start_page > end_page:
    start_page, end_page = end_page, start_page
    print(colored("WARNING: Start page cannot be greater than end page. Swapping start and end pages.", 'yellow'))

# create PdfWriter object
output = PdfWriter()

# add pages to PdfWriter object
for i in range(start_page - 1, end_page):
    output.add_page(pdf_file.pages[i])

# set output file path
pdf_name, pdf_ext = os.path.splitext(os.path.basename(args.pdf_file))
output_file = args.output_file or "{}_{}-{}{}".format(pdf_name, start_page, end_page, pdf_ext)

# check if output file exists
if os.path.isfile(output_file):
    overwrite = input(colored("WARNING: Output file already exists. Do you want to overwrite it? (y/n) ", 'yellow'))
    if overwrite.lower!= 'y':
        print(colored("Aborting. No changes were made.", "red"))
        exit(1)

# write output file
with open(output_file, "wb") as outputStream:
    output.write(outputStream)
    print(colored("Output file saved to {}".format(output_file), 'green'))