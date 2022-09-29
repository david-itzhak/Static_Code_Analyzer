def check_line_length(line_text: str):
    if len(line_text) > 79:
        return True


def check_indentation(line_text: str):
    if (len(line_text) - len(line_text.strip())) % 4 != 0:
        return True


def check_unnecessary_semicolon(line_text: str):
    if line_text.split("#")[0].strip().endswith(';'):
        return True


def check_spaces_before_inline_comments(line_text: str):
    line_text = line_text.lstrip()
    if not line_text.startswith("#") and '#' in line_text and not line_text.split("#")[0].endswith('  '):
        return True


def check_todo(line_text: str):
    if '#' in line_text and 'todo' in line_text.split("#")[1].lower():
        return True


def check_blank_lines_before(blank_lines: int):
    if blank_lines > 2:
        return True


text_analyze_functions = {
    check_line_length: 'S001 Too long',
    check_indentation: 'S002 Indentation is not a multiple of four',
    check_unnecessary_semicolon: 'S003 Unnecessary semicolon',
    check_spaces_before_inline_comments: 'S004 At least two spaces required before inline comments',
    check_todo: 'S005 TODO found'
}


def check_lines(code_lines: str, python_file: str):
    blank_lines = 0
    for line_number, line_text in enumerate(code_lines, start=1):
        if line_text:
            for func, message in text_analyze_functions.items():
                if func(line_text):
                    print(f'{python_file}: Line {line_number}: {message}')
            if check_blank_lines_before(blank_lines):
                print(f'{python_file}: Line {line_number}: S006 More than two blank lines used before this line')
            blank_lines = 0
        else:
            blank_lines += 1
