import init_django_orm  # noqa F401
from db.models import LiteraryFormat, Book, Message, Company, Person, Author


def test():
    # orm-intro -> QuerySets overview ---------------------------------------------------------------------------------
    # django-orm has builtin manager LiteraryFormat.object
    LiteraryFormat.objects.all().delete()
    created_format = LiteraryFormat.objects.create(format="poem")
    print(created_format.format)  # poem
    LiteraryFormat(format="triller").save()

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
        format=LiteraryFormat.objects.get(format="poetry")
    )

    Book.objects.create(
        title="Past",
        price=50,
        size="Kge",
        format=LiteraryFormat.objects.get(format="triller")
    )

    print(Book.objects.all())  # <QuerySet [<Book: Book object (15)>, <Book: Book object (16)>]>
    # -----------------------------------------------------------------------------------------------------------------



    # Fields and Relations -> DateTimeField ---------------------------------------------------------------------------
    Message.objects.all().delete()

    msg = Message.objects.create(
        content="just content",
        # datetime_field=datetime.datetime.now() if didn't specify auto_now=True in models
    )  # datetime.datetime(2023, 1, 11, 18, 1, 22, 159426)  - cause time_zone is USE_TZ = False
    # -----------------------------------------------------------------------------------------------------------------



    # Fields and Relations -> Unique Field ----------------------------------------------------------------------------
    Company.objects.all().delete()

    Company.objects.create(name="Google", description="Big tech company")
    Company.objects.create(name="Googlе", description="Fake")  # error if unique = True
    # django.db.utils.IntegrityError: UNIQUE constraint failed: db_company.name
    # -----------------------------------------------------------------------------------------------------------------



    # Fields and Relations -> save ------------------------------------------------------------------------------------
    Person.objects.all().delete()
    person = Person(name="Kate", age=22)
    person.save()
    person.age += 5
    person.save()
    print(person)  # 1: Kate (age 27)

    person.id = None
    person.save()  # made copy
    person.delete()  # deleted this copy
    #-----------------------------------------------------------------------------------------------------------------


    # Many-to-may ----------------------------------------------------------------------------------------------------

    print(Author.objects.last().book_set)


if __name__ == '__main__':
    test()
