from unittest import TestCase
from user import User


class TestUser(TestCase):
    # setup юзать только тогда, когда данные в тестах не меняются
    # будет запущен перед запуском каждого теста
    # а так лучше юзать например для логиниться
    def setUp(self) -> None:
        # self.user.login()
        self.user = User(
            name="John",
            surname="Smith",
            age=25,
            is_staff=True,
            is_admin=False,
        )

    # будет запущен после запуска каждого теста
    def tearDown(self) -> None:
        # self.user.out()
        del self.user

    # OR below

    # будет запущен один раз перед всеми тестами
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.user = User(
    #         name="John",
    #         surname="Smith",
    #         age=25,
    #         is_staff=True,
    #         is_admin=False,
    #     )
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     del cls.user

    def test_get_info(self):
        # user = User(
        #     name="John",
        #     surname="Smith",
        #     age=25,
        #     is_staff=True,
        #     is_admin=False,
        # )
        self.user_age = 30
        assert self.user.get_info() == "John Smith (age: 30)"

    def test_get_staff_info(self):
        # user = User(
        #     name="John",
        #     surname="Smith",
        #     age=25,
        #     is_staff=True,
        #     is_admin=False,
        # )

        assert self.user.get_staff_info() == "is_staff: True, is_admin: False"

    def test_get_json_data(self):
        user = User(
            name="John",
            surname="Smith",
            age=25,
            is_staff=True,
            is_admin=False,
        )

        assert user.get_json_data() == {
            "name": "John",
            "surname": "Smith",
            "age": 25,
            "is_staff": True,
            "is_admin": False
        }