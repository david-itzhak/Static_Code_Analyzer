import copy

def detect_copy():
    obj = [[]]
    return "shallow copy" if obj[0] is copying_machine(obj)[0] else "deep copy"