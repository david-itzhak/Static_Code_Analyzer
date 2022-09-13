
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


def check_lines_length(code_lines):
    return [i + 1 for i in range(len(code_lines)) if len(code_lines[i]) > 79]


def main():
    code_lines: list[str] = get_code_lines_list()
    too_long_lines: list[int] = check_lines_length(code_lines)
    if too_long_lines:
        for num in too_long_lines:
            print(f'Line {num}: S001 Too long')


if __name__ == '__main__':
    main()