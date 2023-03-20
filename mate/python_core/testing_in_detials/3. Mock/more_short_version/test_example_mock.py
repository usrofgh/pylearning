import pytest

from example_mock import delay
from unittest import mock


@pytest.fixture()
def mocked_sleep():
    with mock.patch("time.sleep") as mocked_sleep:
        yield mocked_sleep


def test_return_function_value(mocked_sleep):
    assert delay(2, lambda: 10) == 10


def test_function_was_called(mocked_sleep):
    #1
    # def mock_function():
    #     mock_function.has_been_called = True
    # mock_function.has_been_called = False
    # delay(3, mock_function)
    # assert mock_function.has_been_called

    #2 + mock in fixture
    mock_function = mock.MagicMock()
    delay(3, mock_function)
    mock_function.assert_called_once()


def test_sleeps(mocked_sleep):
    #1
    # time.sleep = mock.MagicMock()
    # delay(100, lambda: 10)
    # time.sleep.assert_called_once_with(100)

    #2
    # with mock.patch("time.sleep") as mocked_sleep:
    #     delay(100, lambda: 10)
    #     mocked_sleep.assert_called_once_with(100)

    #3
    delay(100, lambda: 10)
    mocked_sleep.assert_called_once_with(100)
