import sys

from termcolor import colored


class Handler:
    @staticmethod
    def handle_error(error_message):
        print(colored(f"ERROR: {error_message}", 'red'))
        sys.exit(1)

    @staticmethod
    def handle_warning(warning_message):
        print(colored(f"ERROR: {warning_message}", 'yellow'))

    @staticmethod
    def handle_info(info_message):
        print(colored(f"ERROR: {info_message}", 'green'))
