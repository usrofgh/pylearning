import datetime

import init_django_orm  # noqa: F401
# from db.models import Car, Message, Company, Person
from db.models import Person, Job


def main():
    # car = Car.objects.create(
    #     brand="Skoda",
    #     horse_power=220,
    #     creation_date="2023-01-01",
    #     market_segment="D"
    # )
    #
    # message = Message.objects.create(
    #     content="Hello, World!",
    # )
    # print(car.get_market_segment_display())  # large car
    # print(message.__dict__)

    # Company.objects.create(
    #     name="Google",  # UNIQUE constraint failed: db_company.name
    #     description="it's a fake"
    # )

    # comp = Company(name="TSMS", description="tech comp").save()
    # print(comp)  # без .save() - tech comp (None). в БД также ничего не добавилось
    # print(comp)  # с .save() - None в БД сохранилось

    # kate = Person(name="Kate", age=22)  # можем работать с экземпляром класса
    # kate.save()
    # print(kate)
    # kate.age += 1  # стало 23
    # kate.save()

    # создаем копию записи с другим id
    # person = Person.objects.get(name="Kate")
    # person.id = None
    # person.save()
#--------------------------------------------------------------------
    # LiteraryFormat.objects.create(
    #     format="Drama"
    # )
    # LiteraryFormat.objects.create(
    #     format="Triller"
    # )
    #
    # Author.objects.create(
    #     first_name="John",
    #     last_name="Silver"
    # )
    #
    # Author.objects.create(
    #     first_name="Doctor",
    #     last_name="Livesey"
    # )

    # book = Book.objects.create(
    #     title="Future",
    #     price=35.68,
    #     format=LiteraryFormat.objects.get("Triller"),
    #     author=[Author.objects.get(first_name="Doctor", last_name="Livesey")]
    # )
    #
    # print(book)

    Job.objects.create(
        title="predictive behavioral assessment",
        description="analyze google/meta data",
        salary=100_572.18
    )
    Job(title="cleaning", salary=27_000.28).save()

    Person.objects.create(
        first_name="Doctor",
        last_name="Silver",
        age=37,
        job=Job.objects.get(id=1)
    )


if __name__ == '__main__':
    main()
