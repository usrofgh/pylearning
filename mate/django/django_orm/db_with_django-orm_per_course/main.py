import init_django_orm  # noqa: F401

from db.models import LiteraryFormat, Car, Message, Company, Person, Book


def main():
    LiteraryFormat.objects.filter().delete()
    print(LiteraryFormat.objects.all())  # <QuerySet [<LiteraryFormat: LiteraryFormat object (1)>]>
    print(LiteraryFormat.objects.create(
        format="drama",
    ))  # LiteraryFormat object (2)

    new_format = LiteraryFormat.objects.create(
        format="poem"
    )
    print(new_format.format)  # poem
    print(LiteraryFormat.objects.get(format="poem").format)  # poem
    filtered_formats = LiteraryFormat.objects.filter(format="poem")
    print(filtered_formats)  # <QuerySet [<LiteraryFormat: LiteraryFormat object (10)>]>






    Car.objects.filter().delete()
    honda = Car.objects.create(
        brand="Honda",
        horse_power=180,
        creation_date="2019-01-01",
        description="This is the best car you ever seen!"
    )
    print(honda)  # 2: Honda (power: 180)
    new_car = Car.objects.create(
        brand="Honda",
        horse_power=180,
        # creation_date="2019-01-01",
    )
    print(new_car)
    new_car = Car.objects.create(
        brand="Honda",
        horse_power=180,
        creation_date="2019-01-01",
        market_segment="D"
    )

    print(new_car.get_market_segment_display())  # large car








    message = Message.objects.create(
        content="Hello, world!",
        # datetime_sent=datetime.datetime.now()  # use it in modules
    )

    print(message.__dict__)









    Company.objects.filter().delete()
    Company.objects.create(
        name="Google",
        description="Big tech company"
    )
    print("Companies: ", Company.objects.all())  # Companies:  <QuerySet [<Company: Google>]>

    Company.objects.create(
        name="Amazon",
        description="Amazing, cloud solutions"
    )

    print("Companies: ", Company.objects.all())  # Companies:  <QuerySet [<Company: Google>, <Company: Google>, <Company: Amazon>]>

    # Company.objects.create(
    #     name="Google",
    #     description="Not a Google, just fake"
    # )  # UNIQUE constraint failed: db_company.name
    # print("Companies: ", Company.objects.all())  # added






    Person.objects.filter().delete()

    person = Person(name="John", age=24)
    print(person)  # None John (age: 24)
    person.save()
    print(person)  # 2 John (age: 24)
    person.age += 1
    person.save()  # change age in DB +1
    print(person)  # 2 John (age: 25)

    person.id = None
    person.save()  # insert a copy


    Book.objects.create(title="Garry Poter", price=15, format_id=160)
    print(Book.objects.get(title="Garry Poter").format)

    format_ = LiteraryFormat.objects.get(format="drama")
    # <class 'django.db.models.
    # fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>
    # print(format_.books)

    # <QuerySet [<Book: Garry Poter (price: 15.00, format: drama)>]>
    print(format_.books.all())

    print(Book.objects.filter(format__format="drama"))  # через FK отримаємо запис в таблиці
    print(str(Book.objects.filter(format__format="drama").query))
    # SELECT "db_book"."id", "db_book"."title", "db_book"."price", "db_book"."format_id"
    # FROM "db_book"
    # INNER JOIN "db_literaryformat"
    # ON ("db_book"."format_id" = "db_literaryformat"."id")
    # WHERE "db_literaryformat"."format" = drama


if __name__ == '__main__':
    main()
