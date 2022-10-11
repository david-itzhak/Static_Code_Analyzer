import itertools

for main_dish, desserts_dish, drinks_dish in itertools.product(
        zip(main_courses, price_main_courses),
        zip(desserts, price_desserts),
        zip(drinks, price_drinks)
):
    price_sum = main_dish[1] + desserts_dish[1] + drinks_dish[1]
    if price_sum <= 30:
        print(main_dish[0], desserts_dish[0], drinks_dish[0], price_sum)
