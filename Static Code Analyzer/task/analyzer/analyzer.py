import re
import ast


def check_line_length(line_text: str, script: str):
    return len(line_text) > 79


def check_indentation(line_text: str, script: str):
    return (len(line_text) - len(line_text.strip())) % 4 != 0


def check_unnecessary_semicolon(line_text: str, script: str):
    return line_text.split("#")[0].strip().endswith(';')


def check_spaces_before_inline_comments(line_text: str, script: str):
    line_text = line_text.lstrip()
    return not line_text.startswith("#") and '#' in line_text and not line_text.split("#")[0].endswith('  ')


def check_todo(line_text: str, script: str):
    return '#' in line_text and 'todo' in line_text.split("#")[1].lower()


def check_blank_lines_before(blank_lines: int):
    return blank_lines > 2


def check_spaces_after_class(line_text: str, script: str):
    return re.match(r'class\s{2,}', line_text.strip())


def check_spaces_after_def(line_text: str, script: str):
    return re.match(r'def\s{2,}', line_text.strip())


def check_class_name_camel_case(line_text: str, script: str):
    return re.match(r'class\s+[a-z]', line_text.strip())


def check_function_name_snake_case(line_text: str, script: str):
    return re.match(r'def\s+[A-Z]', line_text.strip())


def check_argument_name_snake_case(line_text: str, script: str):
    if 'def' not in line_text:
        return False
    temp = re.findall(r'def \w+\(', line_text)
    def_name: str = temp[0][4:-1]
    def_name = def_name.strip()
    tree = ast.parse(script)
    nodes = ast.walk(tree)
    for node in nodes:
        if isinstance(node, ast.FunctionDef) and node.name == def_name:
            args = [a.arg for a in node.args.args]
            for arg in args:
                if re.match(r'.*[A-Z].*', arg):
                    return True
    return False


def check_variable_name_snake_case(line_text: str, script: str):
    if not re.match(r'\w+.=', line_text.strip()):
        return False
    variable = re.search(r'\w+ =', line_text.strip()).group()[:-2]
    if re.fullmatch('[a-z0-9_]+', variable):
        return False
    return True


def check_default_argument_value_is_mutable(line_text: str, script: str):
    if 'def' not in line_text:
        return False
    temp = re.findall(r'def \w+\(', line_text)
    def_name: str = temp[0][4:-1]
    def_name = def_name.strip()
    tree = ast.parse(script)
    nodes = ast.walk(tree)
    for node in nodes:
        if isinstance(node, ast.FunctionDef) and node.name == def_name:
            d_args = [d for d in node.args.defaults]
            args = [a.arg for a in node.args.args]
            for a in d_args:
                if isinstance(a, ast.List):
                    return True
    return False


text_analyze_functions = {
    check_line_length: 'S001 Too long',
    check_indentation: 'S002 Indentation is not a multiple of four',
    check_unnecessary_semicolon: 'S003 Unnecessary semicolon',
    check_spaces_before_inline_comments: 'S004 At least two spaces required before inline comments',
    check_todo: 'S005 TODO found',
    check_spaces_after_class: "S007 Too many spaces after 'class'",
    check_spaces_after_def: "S007 Too many spaces after 'def'",
    check_class_name_camel_case: "S008 Class name should use CamelCase",
    check_function_name_snake_case: "S009 Function name should use snake_case",
    check_argument_name_snake_case: "S010 Argument name should be written in snake_case",
    check_variable_name_snake_case: "S011 Variable should be written in snake_case",
    check_default_argument_value_is_mutable: "S012 The default argument value is mutable"
}


def check_lines(code_lines: str, python_file: str, script: str):
    blank_lines = 0
    for line_number, line_text in enumerate(code_lines, start=1):
        if line_text:
            for func, message in text_analyze_functions.items():
                if func(line_text, script):
                    print(f'{python_file}: Line {line_number}: {message}')
            if check_blank_lines_before(blank_lines):
                print(f'{python_file}: Line {line_number}: S006 More than two blank lines used before this line')
            blank_lines = 0
        else:
            blank_lines += 1
