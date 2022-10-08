from utils import get_code_lines_list, get_python_files, get_path_arg
import os
from analyzer import check_lines


def analyze_file(python_file: str):
    code_lines, script = get_code_lines_list(python_file)
    check_lines(code_lines, python_file, script)


def main():
    path_arg: str = get_path_arg()
    if os.path.isfile(path_arg) and path_arg.endswith('.py'):
        analyze_file(path_arg)
    else:
        python_files = get_python_files(path_arg)
        for python_file in python_files:
            analyze_file(python_file)


if __name__ == '__main__':
    main()