str_1 = input()
str_2 = input()

print(''.join(a + b for a, b in zip(str_1, str_2)))