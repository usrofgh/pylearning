from get_plan import get_plan


def test_should_expected_goals():
    goals = get_plan(500, 3, 50)
    assert goals == [750, 1125, 1687]  # эта проверка
    # включает в себя все предыдущие проверки,
    # if goals == list, then len(list) == 3
    # можно просто оставить один последний тест


