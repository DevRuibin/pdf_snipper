import sys

from termcolor import colored


class Handler:
    @staticmethod
    def handle_error(error_message, end='\n'):
        print(colored(f"ERROR: {error_message}", 'red'), end=end)
        sys.exit(1)

    @staticmethod
    def handle_warning(warning_message, end='\n'):
        print(colored(f"WARNING: {warning_message}", 'yellow'), end=end)

    @staticmethod
    def handle_info(info_message, end='\n'):
        print(colored(f"INFO: {info_message}", 'green'), end=end)
