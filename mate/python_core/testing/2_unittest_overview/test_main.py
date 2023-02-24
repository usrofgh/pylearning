import unittest
import traceback
from main import add, subtract


# В целом main тоже не нужен если запускать с консоли как python -m unittest test_get_plan.py
# в Python любой модуль к-й заканчивается/начинается на test и любой класс с Test - читается тестом для unittest
class TestMain(unittest.TestCase):
    def test_can_add_2_numbers(self):
        # assert add(3, 5) == 8 # юзай assert от unittest
        self.assertEqual(add(3, 5), 8)

    def test_can_subtract_2_numbers(self):
        # assert subtract(3, 5) == -2
        self.assertEqual(subtract(3, 5), -2)


# if __name__ == '__main__':
#     # tests = [test_can_add_2_numbers, test_can_subtract_2_numbers]
#     # for test_function in tests:
#     #     try:
#     #         print(test_function.__name__)
#     #         test_function()
#     #     except Exception:
#     #         print(traceback.format_exc())
#
#     # c unittest вместо всего кода выше просто делаем:
#     unittest.main()
