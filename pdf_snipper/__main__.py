import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from pdf_snipper.snipper import main

main()
