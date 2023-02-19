from get_plan import get_plan

# нужно разбивать тесты на классы эквивалентности


# тут проверяем округление
def test_should_expected_goals_with_rounding():
    goals = get_plan(500, 3, 50)
    assert goals == [750, 1125, 1687]


# тут тест без округления
def test_should_expected_goals_without_rounding():
    goals = get_plan(100, 4, 100)
    assert goals == [200, 400, 800, 1600]


# плохой тест. Тут просто разница в числах, не затрагиваются
# округления, ничего не затрагивается нового, поэтмоу этот тест
# не нужен
def test_should_expected_goals():
    goals = get_plan(200, 3, 50)
    assert goals == [300, 450, 675]


# это тест проверяет крайний случай, этот тест должен быть
def test_should_return_zeros_when_current_production_is_0():
    goals = get_plan(0, 4, 30)
    assert goals == [0, 0, 0, 0]


# новый крайний случай когда все значения == 0
def test_should_return_fixed_goals_when_percent_is_0():
    goals = get_plan(100, 3, 0)
    assert goals == [100, 100, 100]


# + ещё один покрытый крайний случай
def test_should_return_empty_list_when_month_is_0():
    goals = get_plan(100, 0, 40)
    assert goals == []
