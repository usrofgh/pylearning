def cakes(recipe: dict, available: dict) -> int:
    return min([available.get(k, 0) // v for k, v in recipe.items()])

print(cakes( {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
            {"sugar": 500, "flour": 2000, "milk": 2000},))