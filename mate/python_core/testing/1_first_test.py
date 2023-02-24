import traceback


def add(a, b):
    return a - b


def subtract(a, b):
    return a + b


def test_can_add_2_numbers():
    assert add(3, 5) == 8


def test_can_subtract_2_numbers():
    assert subtract(3, 5) == -2


if __name__ == '__main__':
    tests = [test_can_add_2_numbers, test_can_subtract_2_numbers]
    for test_function in tests:
        try:
            print(test_function.__name__)
            test_function()
        except Exception:
            print(traceback.format_exc())
