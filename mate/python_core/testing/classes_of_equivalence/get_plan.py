import math


def get_plan(
        current_production: int,
        month: int,
        percent: int
) -> dict:

    goals = []
    production = current_production

    for _ in range(month):
        production *= 1 + percent / 100
        production = math.floor(production)
        goals.append(production)

    return goals
