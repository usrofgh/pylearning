import re


def add_css_class(element: dict, class_to_add: str) -> None:
    # classes = set(element["class_name"].split())
    # classes.add(class_to_add)
    # element["class_name"] = " ".join(classes)

    # element["class_name"] = element["class_name"].strip()
    # element["class_name"] = re.sub(" +", " ", element["class_name"])
    #
    # if class_to_add not in element["class_name"].split():
    #     element["class_name"] += f" {class_to_add}"

    # выше код, кажется что все должно быть ок, тестирую. Тесты
    # отловили проблему что результат в другой последовательности
    # поэтому меняем set как ниже

    classes = dict.fromkeys(element["class_name"].split())
    classes[class_to_add] = None
    element["class_name"] = " ".join(classes.keys())  # теперь ок


# При рефакторинге удобно чтобы были уже написаны тесты
el = {
    "class_name": "joke new"
}

add_css_class(el, "action")  # joke new active
add_css_class(el, "new")  # joke new active


# How to group tests
# не ясно какой тест какую функцию тестирует https://prnt.sc/aK08ZGcyAFdh
# их нужно разбить по группам(классам)
def remove_css_class(element: dict, class_to_remove: str):
    classes = dict.fromkeys(element["class_name"].split())
    if class_to_remove in classes:
        del classes[class_to_remove]
    element["class_name"] = " ".join(classes.keys())
