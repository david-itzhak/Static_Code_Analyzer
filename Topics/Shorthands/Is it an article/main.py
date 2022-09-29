import re

word = input()
print(re.match(r'the\Z', word) is not None)