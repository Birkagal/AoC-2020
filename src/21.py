from collections import defaultdict
'''
Part One - Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?
Part Two - What is your canonical dangerous ingredient list?
'''


def parse_data(data):
    recipes = []
    possible_allergens = defaultdict(set)
    recipe_with_allergen = defaultdict(list)
    for index, line in enumerate(data):
        ingredients, allergens = line.rstrip(')\n').split(' (contains ')
        ingredients = set(ingredients.split())
        allergens = set(allergens.split(', '))
        recipes.append(ingredients)

        for aller in allergens:
            recipe_with_allergen[aller].append(index)

        for ingr in ingredients:
            possible_allergens[ingr] |= allergens

    return recipes, possible_allergens, recipe_with_allergen


def find_safe_ingredients(recipes, possible_allergens, recipe_with_allergen):
    safe_ingredients = []

    for ingr, possible_aller in possible_allergens.items():
        possible_aller = possible_allergens[ingr]
        impossible = set()

        for aller in possible_aller:
            for i in recipe_with_allergen[aller]:
                if ingr not in recipes[i]:
                    impossible.add(aller)
                    break

        possible_aller -= impossible

        if not possible_aller:
            safe_ingredients.append(ingr)

    return safe_ingredients


def find_corrent_ingredients(possible_aller):
    assigned = dict()

    while possible_aller:
        for ingr, possible in possible_aller.items():
            if len(possible) == 1:
                break
        aller = possible.pop()
        assigned[aller] = ingr
        del possible_aller[ingr]

        for ingr, possible in possible_aller.items():
            if aller in possible:
                possible.remove(aller)

    return assigned


def partOne(content):
    recipes, possible_allergens, recipe_with_allergen = parse_data(content)
    safe_ingredients = find_safe_ingredients(
        recipes, possible_allergens, recipe_with_allergen)
    return sum(ingr in r for r in recipes for ingr in safe_ingredients)


def partTwo(content):
    recipes, possible_allergens, recipe_with_allergen = parse_data(content)
    safe_ingredients = find_safe_ingredients(
        recipes, possible_allergens, recipe_with_allergen)

    for ingr in safe_ingredients:
        del possible_allergens[ingr]

    assigned = find_corrent_ingredients(possible_allergens)
    return ','.join(map(assigned.get, sorted(assigned)))
