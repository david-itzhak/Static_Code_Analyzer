import math


# Modify this function in the shell and copy the new version here
def my_sqrt(value):
    if isinstance(value, str):
        return "The string should be converted into a numeric data type"
    if isinstance(value, (int, float)):
        return math.sqrt(value)
    return None
