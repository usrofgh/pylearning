import datetime

from django.db import IntegrityError

import init_django_orm  # noqa F401
from db.models import LiteraryFormat, Book, Message


def main():
    # orm-intro -> QuerySets overview ---------------------------------------------------------------------------------
    # django-orm has builtin manager LiteraryFormat.object
    LiteraryFormat.objects.all().delete()
    created_format = LiteraryFormat.objects.create(format="poem")
    print(created_format.format)  # poem

    got_format = LiteraryFormat.objects.get(format="poem")
    print(got_format)  # LiteraryFormat object (1)
    print(got_format.format)  # poem

    filtered_formats = LiteraryFormat.objects.filter(format="poem")
    print(filtered_formats)  # <QuerySet [<LiteraryFormat: LiteraryFormat object (1)>]>
    # QuerySet - абстракция вокруг SQL, за генерацию запроса отвечает QueryBuilder ответ к-го QueryBuilder
    # посмотреть сгенерированный код можно через debugging
    filtered_formats.update(format="poetry")  # updated
    # -----------------------------------------------------------------------------------------------------------------



    # Fields and Relations -> File choices ----------------------------------------------------------------------------
    Book.objects.all().delete()
    Book.objects.create(
        title="Future",
        price=32.58,
    )

    Book.objects.create(
        title="Past",
        price=50,
        size="Kge",
    )

    print(Book.objects.all())  # <QuerySet [<Book: Book object (15)>, <Book: Book object (16)>]>
    # -----------------------------------------------------------------------------------------------------------------


    # Fields and Relations -> DateTimeField ---------------------------------------------------------------------------

    msg = Message.objects.create(
        content="just content",
        datetime_field=datetime.datetime.now()
    )  # datetime.datetime(2023, 1, 11, 18, 1, 22, 159426)  - cause time_zone is USE_TZ = False
    print(msg.__dict__)


if __name__ == '__main__':
    main()
