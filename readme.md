# PDF Snipper

PDF Snipper is a command-line tool for extracting a range of pages from a PDF file and saving them as a new PDF file.

## Installation

To install PDF Snipper, simply download the `pdf_snipper.py` file and place it in a directory of your choice. You can then run the tool using the command:

```bash
python pdf_snipper --help
```

## Usage

To use PDF Snipper, run the command:

```bash
python pdf_snipper snipper  --start_page START_PAGE --end_page END_PAGE --input PDF_FILE_PATH [--output OUTPUT_FILE_PATH]
```

- `START_PAGE`: the starting page number to extract (inclusive).
- `END_PAGE`: the ending page number to extract (inclusive).
- `PDF_FILE_PATH`: the path to the PDF file to extract pages from.
- `OUTPUT_FILE_PATH` (optional): the path to save the extracted pages as a new PDF file. If not specified, the output file will be saved in the same directory as the input file with a filename based on the start and end page numbers.

### Examples

Extract pages 5-10 from the input PDF file and save as a new file:

```bash
python pdf_snipper snipper --start_page 5 --end_page 10 --input input.pdf --output output.pdf
```

Extract pages 1-3 from the input PDF file and save as a new file in the same directory as the input file:

```bash
python pdf_snipper --start_page 1 --end_page 3 --input input.pdf
```
## Additional Features

PDF Snipper can be extended to include additional features, such as:

1. Merge PDF files: allow users to merge multiple PDF files into a single PDF file.
2. Split by bookmark: allow users to split a PDF file into multiple files based on its bookmarks.
3. Rotate pages: allow users to rotate pages in a PDF file.
4. Add watermarks: allow users to add watermarks to a PDF file.
5. Extract text: allow users to extract text from a PDF file.
6. OCR: use optical character recognition (OCR) to recognize text in scanned PDFs.
7. Command-line options for more customization: add more command-line options to allow users to customize the output file name, page size, and other properties.


## Error Handling

PDF Snipper will handle certain errors that may occur during execution. If an error occurs, the tool will print an error message and exit with a non-zero status code. Some of the errors that are handled include:

- Invalid input parameters: if the start or end page numbers are invalid or if the input PDF file cannot be found.
- Invalid output file path: if the output file path is invalid or if the specified output file already exists and the user chooses not to overwrite it.

## License

PDF Snipper is licensed under the MIT license. See the `LICENSE` file for more information.
