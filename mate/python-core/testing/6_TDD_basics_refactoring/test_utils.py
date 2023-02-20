import pytest
from utils import add_css_class, remove_css_class


# TDD - Test-driven development
# принцип разработки через тестирование
# не пишем ни одной строчки реализации пока нет теста к-й не проходит
# если все тесты прошли - реализация правильная.

# Каждый тест состоит из 3-х этапов


class TestAddCssClass:
    # с какого теста начать?:
    def test_should_add_new_class(self):
        # Подготовка
        el = {
            "class_name": "joke new"
        }
        # Действие
        add_css_class(el, "active")
        # Проверка
        assert el["class_name"] == "joke new active"

    def test_should_not_add_existing_class(self):
        el = {
            "class_name": "joke new"
        }

        add_css_class(el, "new")
        assert el["class_name"] == "joke new"

    def test_should_add_class_which_is_part_of_another_one(self):
        el = {
            "class_name": "joke new active"
        }

        add_css_class(el, "ok")
        assert el["class_name"] == "joke new active ok"

    def test_should_remove_extra_outer_spaces(self):
        el = {
            "class_name": "  joke new   "
        }
        add_css_class(el, "active")
        assert el["class_name"] == "joke new active"

    def test_should_remove_extra_inner_spaces(self):
        el = {
            "class_name": "joke    new"
        }
        add_css_class(el, "active")
        assert el["class_name"] == "joke new active"

    def test_should_remove_extra_spaces_when_new_class_not_add(self):
        el = {
            "class_name": "  joke    new    active  "
        }
        add_css_class(el, "active")
        assert el["class_name"] == "joke new active"

    # How to check that error was raised
    def test_should_raise_error_if_class_name_key_not_exist(self):
        el = {}

        with pytest.raises(KeyError):
            add_css_class(el, "joke")

    def test_should_raise_error_if_class_name_is_integer(self):
        el = {
            "class_name": 1
        }

        with pytest.raises(AttributeError):
            add_css_class(el, "joke")


# Refactoring
class TestRemoveCssClass:
    def test_should_remove_existing_class(self):
        el = {
            "class_name": "joke new"
        }

        remove_css_class(el, "joke")
        assert el["class_name"] == "new"

    def test_should_remove_extra_spaces(self):
        el = {
            "class_name": "  joke    new  "
        }

        remove_css_class(el, "joke")
        assert el["class_name"] == "new"

    def test_should_remove_all_occurrences(self):
        el = {
            "class_name": "joke new joke joke"
        }

        remove_css_class(el, "joke")
        assert el["class_name"] == "new"

    def test_should_remove_duplicates_of_other_classes(self):
        el = {
            "class_name": "hello joke new joke joke"
        }

        remove_css_class(el, "joke")
        assert el["class_name"] == "hello new"