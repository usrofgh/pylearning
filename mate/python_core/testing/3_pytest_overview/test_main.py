# pytest test_get_plan.py
# pytest function-based


from main import add, subtract


def test_can_add_2_numbers():
    assert add(3, 5) == 8


def test_can_subtract_2_numbers():
    assert subtract(3, 5) == -2
