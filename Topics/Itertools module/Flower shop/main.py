import itertools


for x in range(1, 4):
    bouquets = itertools.combinations(flower_names, x)
    print(*bouquets, sep='\n')

