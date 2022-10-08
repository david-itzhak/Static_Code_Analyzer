import sys
n = int(input())


def even():
    num = 0
    while True:
        yield num
        num += 2


# Don't forget to print out the first n numbers one by one here

generator = even()
for _ in range(n):
    print(next(generator))
