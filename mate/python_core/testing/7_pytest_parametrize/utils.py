import re

# К примеру новый запрос, "classes" заменить на classes. Вручную делать оч долго
# с рефакторингом можно забыть изменить в каком-то файле
# но чт если теперь менять нужно лишь в том случае, если is_hidden = False
# тогда в кадый тест в el придется добавлять is_hidden, а что если тестов 500?
# Проблема в том, что все те тесты - дублирование кода, все что отличается - строка с классами
# новый аргумент в add_css_class и expected result, Другое - копия

# разбиваю тесты на 2 группы


def add_css_class(element: dict, class_to_add: str) -> None:
    if not element["is_hidden"]:
        classes = dict.fromkeys(element["classes"].split())
        classes[class_to_add] = None
        element["classes"] = " ".join(classes.keys())


el = {
    "class_name": "joke new joke",
    "is_hidden": False,
}