from sys import argv
from argument_error import ArgumentError
import os


def get_code_lines_list(path: str) -> list[str]:
    file_text: str = None
    while not file_text:
        try:
            with open(path, 'r') as checked_file:
                file_text = checked_file.read()
            code_lines = file_text.splitlines()
            return code_lines, file_text
        except Exception as err:
            print(err)


def get_path_arg():
    args = argv
    if len(args) > 1:
        return args[1]
    else:
        raise ArgumentError


def get_python_files(directory_path):
    with os.scandir(directory_path) as entries:
        return [directory_path + '\\' + entry.name for entry in entries if entry.is_file() and entry.name.endswith('.py')]