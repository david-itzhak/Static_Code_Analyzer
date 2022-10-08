import ast

tree = ast.parse(code)
nodes = ast.walk(tree)
call_nodes = []
for node in nodes:
    if isinstance(node, ast.Call):
        call_nodes.append(node.func.id)
print(call_nodes)