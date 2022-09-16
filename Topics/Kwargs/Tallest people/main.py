def tallest_people(**people):
    people_sorted = sorted(people.items())
    max_h = max(people.values())
    for n, h in people_sorted:
        if h == max_h:
            print(f'{n} : {h}')
