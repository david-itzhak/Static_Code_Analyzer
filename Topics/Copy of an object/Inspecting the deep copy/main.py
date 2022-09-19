import copy


def solve(obj):
    return id(copy.deepcopy(obj)) != id(obj)
    # return obj is not copy.deepcopy(obj)