import pytest

from user import User

# Идея фикстуры в том, что мы можем юзать какую угодно фикстуру когда она нужна, а когда не нужна - не указывать

# запускается каждый раз перед каждым тестом
# как сделать аналог tearDown? - yield
@pytest.fixture()  # if add scope="module" then fixture will run once berore and after all tests
def user_template() -> User:
    print("Before test")
    # login
    yield User(
        name="John",
        surname="Smith",
        age=25,
        is_staff=True,
        is_admin=False,
    )
    # logout
    print("After test")


@pytest.fixture()
def another_user() -> User:
    print("Bob created")
    yield User(
        name="Bob",
        surname="Black",
        age=40,
        is_staff=True,
        is_admin=False,
    )


class TestUser:
    # user_template не функция, а пользователь
    # нужно чтобы не дублировать создание User в каждом тесте
    # так как если не дублировать, то при смене значений аттрибутов
    # экз. класса юзера оно изменится везде, и тесты завалятся
    def test_get_info(self, user_template, another_user):
        user_template.age = 18
        assert user_template.get_info() == "John Smith (age: 18)"
        assert another_user.get_info() == "Bob Black (age: 40)"  # сразу два теста в одном, бывает не часто

    def test_get_staff_info(self, user_template):
        assert user_template.get_staff_info() == "is_staff: True, is_admin: False"

    def test_get_json_data(self, user_template):
        assert user_template.get_json_data() == {
            "name": "John",
            "surname": "Smith",
            "age": 25,
            "is_staff": True,
            "is_admin": False
        }
