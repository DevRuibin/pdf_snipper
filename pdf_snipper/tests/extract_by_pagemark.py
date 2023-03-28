from typing import List

import PyPDF2
from PyPDF2.generic._data_structures import Destination


def get_bookmarks(bookmark: Destination, bookmarks: List[Destination], level: int = 0,
                  max_level: int = 0) -> Destination:
    if bookmark is None:
        raise ValueError("bookmark is None")
    if isinstance(bookmark, Destination):
        bookmark.title = "*" * level + bookmark.title
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
                get_bookmarks(bookmark[i], bookmarks, level + 1, max_level)
                i += 1
            else:
                i += 1

    return None


# Open the input PDF file
with open('Theartofmulticore.pdf', 'rb') as input_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(input_file)

    # Get the root bookmark object
    root_bookmark = pdf_reader.outline

    # Print the titles of all bookmarks
    bookmarks = []
    get_bookmarks(root_bookmark, bookmarks, max_level=3)
    for bookmark in bookmarks:
        print(bookmark.title)
        # print(bookmark.page)
