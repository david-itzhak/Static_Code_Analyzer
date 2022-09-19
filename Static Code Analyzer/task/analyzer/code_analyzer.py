from sys import argv
from argument_error import ArgumentError


def get_path() -> str:
    path = input()
    while path == '':
        print("The empty input. The path to the file can't be empty")
        path = input()
    return path


def get_code_lines_list() -> list[str]:
    file_text: str = None
    while not file_text:
        path: str = get_path()
        try:
            with open(path, 'r') as checked_file:
                file_text = checked_file.read()
            code_lines = file_text.splitlines()
            return code_lines
        except Exception as err:
            print(err)


def check_line_length(line_number: int, line_text: str):
    if len(line_text) > 79:
        print(f'Line {line_number}: S001 Too long')


def check_indentation(line_number: int, line_text: str):
    if (len(line_text) - len(line_text.strip())) % 4 != 0:
        print(f'Line {line_number}: S002 Indentation is not a multiple of four')


def check_unnecessary_semicolon(line_number: int, line_text: str):
    if line_text.split("#")[0].strip().endswith(';'):
        print(f'Line {line_number}: S003 Unnecessary semicolon')


def check_spaces_before_inline_comments(line_number: int, line_text: str):
    line_text = line_text.lstrip()
    if not line_text.startswith("#") and '#' in line_text and not line_text.split("#")[0].endswith('  '):
        print(f'Line {line_number}: S004 At least two spaces required before inline comments')


def check_todo(line_number: int, line_text: str):
    if '#' in line_text and 'todo' in line_text.split("#")[1].lower():
        response = f'Line {line_number}: S005 TODO found'
        print(response)
        return response


def check_blank_lines_before(line_number: int, blank_lines: int):
    if blank_lines > 2:
        print(f'Line {line_number}: S006 More than two blank lines used before this line')


def check_lines(code_lines):
    blank_lines = 0
    for line_number, line_text in enumerate(code_lines, start=1):
        if line_text.split():
            check_line_length(line_number, line_text)
            check_indentation(line_number, line_text)
            check_unnecessary_semicolon(line_number, line_text)
            check_spaces_before_inline_comments(line_number, line_text)
            check_todo(line_number, line_text)
            check_blank_lines_before(line_number, blank_lines)
            blank_lines = 0
        else:
            blank_lines += 1


def get_directory_path():
    args = argv
    if len(args) > 1:
        return args[1]
    else:
        raise ArgumentError


def main():
    directory_path = get_directory_path()
    code_lines: list[str] = get_code_lines_list()
    check_lines(code_lines)


if __name__ == '__main__':
    main()