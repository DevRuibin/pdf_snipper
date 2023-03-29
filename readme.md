# PDF Snipper

PDF Snipper is not only a snipper. It is a command-line tool that offers a range of features for manipulating PDF files. The tool was initially designed to extract a range of pages from a PDF file and save them as a new file, but it is becoming a tool box.  You can call it PDF commander

## Installation

To install PDF Snipper, see the [`install.sh`](./install.sh)

## Usage

You can use `python pdf_snipper -h` to get a very detail information.

PDF Snipper offers the following command-line options:

1. **Snipper:** Extract a range of pages from a PDF file and save them as a new file.

   ```bash
   python pdf_snippery snipper --start_page START_PAGE --end_page END_PAGE --input PDF_FILE_PATH [--output OUTPUT_FILE_PATH]
   ```

   - `START_PAGE`: the starting page number to extract (inclusive).
   - `END_PAGE`: the ending page number to extract (inclusive).
   - `PDF_FILE_PATH`: the path to the PDF file to extract pages from.
   - `OUTPUT_FILE_PATH` (optional): the path to save the extracted pages as a new PDF file. If not specified, the output file will be saved in the same directory as the input file with a filename based on the start and end page numbers.

   Examples

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

## License

PDF Snipper is licensed under the MIT license. See the `LICENSE` file for more information.

