import itertools


print("\n".join("{} {}".format(*names) for names in itertools.product(first_names, middle_names)))