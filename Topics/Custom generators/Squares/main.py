n = int(input())


def squares():
    current_int = 1
    while True:
        yield current_int ** 2
        current_int += 1


# Don't forget to print out the first n numbers one by one here
gen = squares()
for _ in range(n):
    print(next(gen))
