from typing import List

from PyPDF2 import PdfReader
from PyPDF2.generic import Destination
from pdf_snipper.snipper_utils.tool import Tool

from pdf_snipper.snipper_error.handler import Handler

class PdfBookmark(Tool):
    def __init__(self, args):
        super().__init__()
        self.args = args
        self.pdf_file = args.pdf_file
        self.max_level = args.max_level
        # check arguments
        self.check_args()

    def get_bookmarks(self, bookmark, bookmarks: List[Destination], level: int = 0,
                      max_level: int = 0):
        if bookmark is None:
            raise ValueError("bookmark is None")
        if isinstance(bookmark, Destination):
            bookmarks.append(bookmark)
            return bookmark
        if isinstance(bookmark, list):
            i = 0
            mark_len = len(bookmark)
            while i < mark_len:
                if isinstance(bookmark[i], Destination):
                    bookmarks.append(bookmark[i])
                    i += 1
                elif isinstance(bookmark[i], list) and (level < max_level):
                    self.get_bookmarks(bookmark[i], bookmarks, level + 1, max_level)
                    i += 1
                else:
                    i += 1

        return bookmarks
    def check_args(self):
        if self.max_level is None:
            self.max_level = 0
        if self.max_level < 0:
            Handler.handle_warning("WARNING: max_level must be greater than 0. Setting max_level to 0.")
            Handler.handle_warning("Continue with max_level = 0(first level only) (y/n)?", end=" ")
            if input().lower() != "y":
                Handler.handle_info("Exiting...")
            self.max_level = 0

    def run(self):

        # read input PDF file
        pdf_file = PdfReader(open(self.pdf_file, "rb"))
        if self.args.bookmark:
            root_bookmark = pdf_file.outline
            bookmarks = []
            self.get_bookmarks(root_bookmark, bookmarks, max_level=self.max_level)
            for bookmark in bookmarks:
                print(bookmark.title, end=" ")
                if bookmark.page is not None:
                    print(pdf_file.get_page_number(bookmark.page))
                else:
                    print()
        else:
            Handler.handle_error("No option selected. Use bookmark -h for help.")

