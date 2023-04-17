# PDF Snipper

PDF Snipper is not only a snipper. It is a command-line tool that offers a range of features for manipulating PDF files. The tool was initially designed to extract a range of pages from a PDF file and save them as a new file, but it is becoming a tool box. You can call it PDF commander. The tool allows users to extract a range of pages from a PDF file, merge multiple PDF files into one, read bookmarks to a PDF file, and more.

## Installation

To install PDF Snipper, see the [`install.sh`](https://chat.openai.com/install.sh) file.

## Usage

PDF Snipper offers the following command-line options:

### Snipper

Extracts a range of pages from a PDF file and saves them as a new file.

```bash
python pdf_snipper snipper [-h] [-s START_PAGE] [-e END_PAGE] [-i PDF_FILE] [-o OUTPUT_FILE] [-p PAGES [PAGES ...]]
```

Arguments:

- `-s`, `--start_page`: Starting page number to extract (inclusive).
- `-e`, `--end_page`: Ending page number to extract (inclusive).
- `-i`, `--input`: Path to the input PDF file.
- `-o`, `--output`: Path to the output PDF file. If not specified, the output file will be saved in the same directory as the input file with a filename based on the start and end page numbers.
- `-p`, `--pages`: List of page numbers to extract.

### Merge

Merges multiple PDF files into one PDF file.

```bash
python pdf_snipper merge [-h] -i INPUT_FILES [INPUT_FILES ...] [-o OUTPUT_FILE]
```

Arguments:

- `-i`, `--input`: List of paths to the input PDF files.
- `-o`, `--output`: Path to the output PDF file.

### Bookmark

Bookmark operations

```bash
python pdf_snipper bookmark [-h] [-i PDF_FILE] [-o OUTPUT_FILE] [-m] [-M MAX_LEVEL]
```

Arguments:

- `-i`, `--input`: Path to the input PDF file.
- `-o`, `--output`: Path to the output PDF file.  Base now, this flag can be ignored.
- `-m`, `--bookmark`: Flag to read bookmarks.
- `-M`, `--max_level`: Maximum bookmark level.

Run `pdf_snipper -h` to see more information about each command.

## Additional Features

PDF Snipper can be extended to include additional features, such as:

1. Split by bookmark: allow users to split a PDF file into multiple files based on its bookmarks.
2. Rotate pages: allow users to rotate pages in a PDF file.
3. Add watermarks: allow users to add watermarks to a PDF file.
4. Extract text: allow users to extract text from a PDF file.
5. OCR: use optical character recognition (OCR) to recognize text in scanned PDFs.
6. Command-line options for more customization: add more command-line options to allow users to customize the output file name, page size, and other properties.
7. Format convertor: Convert files in other formats to PDF files.

## License

PDF Snipper is licensed under the MIT license. See the `LICENSE` file for more information.
