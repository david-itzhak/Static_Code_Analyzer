import re

# your code here
word = input()

print(True if re.match('\w+-\w+', word) else False)