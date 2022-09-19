# sorting function
def ___(_):
    _____ = len(_)
    for __ in range(_____ - 1):
        for ____ in range(_____ - __ - 1):
            if _[____] > _[____ + 1]:
                _[____], _[____ + 1] = _[____ + 1], _[____]
    return _

# where copying takes place
__ = [int(_) for _ in input().split()]
____ = ___(__.copy())

if __ == ____:
    print('sorted')
else:
    print('not sorted')