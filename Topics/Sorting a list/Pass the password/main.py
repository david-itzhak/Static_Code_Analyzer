# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

# your code below
print('\n'.join(f'{el} {len(el)}' for el in sorted(passwords, key=len)))