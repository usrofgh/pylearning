import pytest
from utils import add_css_class


class TestAddCssClass:

    # проверяет что после изменения значение корректно
    # все эти таплы считаются за различные тесты
    @pytest.mark.parametrize(
        "initial_classes,class_to_add,expected_classes",
        # список случаев к-е я буду обрабатывать, list(tuple)
        [
            # входные данные для первого теста test_should_add_new_class
            # pytest.param нужен чтобы в конце написать называние теста
            pytest.param(
                "joke new",
                "active",
                "joke new active",
                id="should add new class"
            ),
            pytest.param(
                "joke new",
                "new",
                "joke new",
                id="should not add existing class"
            ),
            pytest.param(
                "joke new active",
                "ok",
                "joke new active ok",
                id="should add class which is part of another one"
            )
        ]
    )
    def test_modify_classes_correctly(
        self,
        initial_classes,
        class_to_add,
        expected_classes
    ):
        el = {
            "classes": initial_classes,
            "is_hidden": False
        }

        add_css_class(el, class_to_add)
        assert el["classes"] == expected_classes

    @pytest.mark.parametrize(
        "initial_element,expected_error",
        [
            pytest.param(
                {"is_hidden": False},
                KeyError,
                id="Should raise error when no key `classes`"

            ),
            pytest.param(
                {"classes": 1, "is_hidden": False},
                AttributeError,
                id="Should raise error when `classes` in integer"
            )
        ]
    )
    def test_raising_error_correctly(
            self,
            initial_element,
            expected_error
    ):
        with pytest.raises(expected_error):
            add_css_class(initial_element, "")


# реализовывал через parametrize
#     def test_should_add_new_class(self):
#         el = {
#             "class_name": "joke new"
#         }
#         add_css_class(el, "active")
#         assert el["class_name"] == "joke new active"
#
#     def test_should_not_add_existing_class(self):
#         el = {
#             "class_name": "joke new"
#         }
#
#         add_css_class(el, "new")
#         assert el["class_name"] == "joke new"
#
#     def test_should_add_class_which_is_part_of_another_one(self):
#         el = {
#             "class_name": "joke new active"
#         }
#
#         add_css_class(el, "ok")
#         assert el["class_name"] == "joke new active ok"