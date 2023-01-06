import init_django_orm  # noqa: F401

from db.models import LiteraryFormat


def main():
    # у django встроенный manager LiteraryFormat.object
    # для подсветки нужен pycharm pro

    # records = LiteraryFormat.objects.all()

    # new_format = LiteraryFormat.objects.create(
    #     format="poema",
    # )
    # print(new_format.format)

    # poem_format = LiteraryFormat.objects.get(
    #     format="poema",
    # )
    # print(poem_format)  # LiteraryFormat object (3)
    # print(poem_format.format)  # poema

    filtered_formats = LiteraryFormat.objects.filter(
        format="poetry",
    )#.update(format="poetry")  # update возвращает к-во э-тов к-е он обновил
    print(filtered_formats)  # <QuerySet [<LiteraryFormat: LiteraryFormat object (3)>]> - за генерацию запросов к БД
    # отвечает querybuilder к-й возвращает queryset(абстракция над sql) -можно посмотреть какой там sql код через debug

    LiteraryFormat.objects.filter(
        format="drama",
    ).delete()  # профильтруем по drama и удалим


if __name__ == '__main__':
    main()
