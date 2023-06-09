from pdf_snipper.snipper_error.handler import Handler
from pdf_snipper.snipper_utils.pdf_snipper import PdfSnipper
from pdf_snipper.snipper_utils.pdf_merge import PdfMerge
from pdf_snipper.snipper_utils.pdf_bookmark import PdfBookmark
import argparse


def main():

    # Map command to respective class
    tool_classes = {'snipper': PdfSnipper, 'merge': PdfMerge, 'bookmark': PdfBookmark}

    # Create the main argument parser
    parser = argparse.ArgumentParser(description='PDF Snipper - command-line PDF manipulation tool')
    subparsers = parser.add_subparsers(dest='command', help=f'Command to execute ({tool_classes.keys()})')

    # Create parser for 'snipper' command
    snipper_parser = subparsers.add_parser('snipper', aliases=['extract', "cut"],
                                           help='Extract a range of pages from a PDF file')
    snipper_parser.add_argument('-s', '--start_page', type=int, help='Starting page number (inclusive)')
    snipper_parser.add_argument('-e', '--end_page', type=int, help='Ending page number (inclusive)')
    snipper_parser.add_argument('-i', '--input', dest='pdf_file', type=str, help='Path to the input PDF file')
    snipper_parser.add_argument('-o', '--output', dest='output_file', type=str, help='Path to the output PDF file')
    snipper_parser.add_argument('-p', '--pages', nargs='+', type=int, help='List of page numbers to extract')

    # Create parser for 'merge' command
    merge_parser = subparsers.add_parser('merge', help='Merge multiple PDF files into one PDF file')
    merge_parser.add_argument('-i', '--input', nargs='+', dest='pdf_files', type=str, required=True,
                              help='List of paths to the input PDF files')
    merge_parser.add_argument('-o', '--output', dest='output_file', type=str, help='Path to the output PDF file')

    # Create parser for 'bookmark' command
    bookmark_parser = subparsers.add_parser('bookmark', help='Bookmark operations')
    bookmark_parser.add_argument('-i', '--input', dest='pdf_file', type=str, help='Path to the input PDF file')
    bookmark_parser.add_argument('-o', '--output', dest='output_file', type=str, help='Path to the output PDF file')
    bookmark_parser.add_argument('-m', '--bookmark', dest='bookmark', action='store_true', help='Bookmark to add')
    bookmark_parser.add_argument('-M', '--max_level', dest='max_level', type=int, help='Maximum bookmark level')


    # Parse the command-line arguments
    args = parser.parse_args()
    if not args.command:
        Handler.handle_error("Please provide a command to execute. Usage: pdf_snipper <command>")
        return

    # Call the appropriate class based on the user's input
    if args.command not in tool_classes:
        Handler.handle_error('Invalid command: {}'.format(args.command))
    else:
        tool_class = tool_classes[args.command]
        tool = tool_class(args)
        tool.run()


if __name__ == '__main__':
    main()
