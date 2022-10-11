import itertools

# print(*itertools.combinations(teams, 2), sep="\n")
my_iter = itertools.combinations(teams, 2)

for teams_pair in my_iter:
    print(teams_pair)
