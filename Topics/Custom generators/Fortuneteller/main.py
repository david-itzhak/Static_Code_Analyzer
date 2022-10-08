number = input()


def digit_letters(number_sting):
    yield from number_sting


print(sum([int(n) for n in digit_letters(number)]))
