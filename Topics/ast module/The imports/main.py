import ast

tree = ast.parse(code)
nodes = ast.walk(tree)
for node in nodes:
    if isinstance(node, ast.Import):
        for name in node.names:
            print(name.name)
