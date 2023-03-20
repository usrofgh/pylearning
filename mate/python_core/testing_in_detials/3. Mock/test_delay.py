from unittest import mock

import pytest

from delay import delay
#A mock object replaces and imitates a real object during the test.



# в любом тесте где фикстура time не будет долгого ожидания sleep
# теперь можно убрать CM с моками
@pytest.fixture()
def mocked_sleep():
    with mock.patch("time.sleep") as mock_test_sleep:
        yield mock_test_sleep


def test_return_function_value(mocked_sleep):
    assert delay(2, lambda: 10) == 10


def test_function_was_called(mocked_sleep):
    # проверяет была ли вызвана функция.
    # mock обязательно, может подменять логику работы ф-ии

    # вместо того как ниже проще юзать модуль mock

    # def mock_function():
    #     mock_function.has_been_called = True
    #
    # mock_function.has_been_called = False
    # delay(3, mock_function)
    # assert mock_function.has_been_called

    mock_function = mock.MagicMock()
    delay(3, mock_function)
    mock_function.assert_called_once()


def test_sleeps(mocked_sleep):
    # time.sleep = mock.MagicMock()
    # delay(100, lambda: None)  # теперь не жду 100 сек, так как
    # # когда мокаю time.sleep, сама ф-я sleep не вызывается
    # # magicMock() подменил реализацию, и с помощью него я просто
    # # проверяю что эта ф-я вызывалась
    #
    # # time.sleep.assert_called_once()  # теперь это MagicMock
    # time.sleep.assert_called_once_with(100)  # лучше эту тут
    # # чтобы убедиться что 100 передается в sleep в моей delay

    # но что если бы дальше я хотел юзать прваильно sleep, не
    # mockom? Также выше пришлось импортировать time к-й
    # больше нигде не юзаю. А что если бы нужно мокать свой
    # проект, что, нужно было бы мокать весь проект?
    # поэтому лучше юзать как ниже

    # mocked_sleep - analog time.sleep = mock.MagicMock()
    # внутри CM будет замоканый, снаружи - нет
    # с fixture mocked CM не нужен
    # with mock.patch("time.sleep") as mocked_sleep:
    delay(100, lambda: None)
    mocked_sleep.assert_called_once_with(100)
