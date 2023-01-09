import init_django_orm  # noqa: F401

from db.models import Person


def main():
    records = Person.objects.get(
        first_name="albert",
        last_name="shevchenko",
    )
    print(Person.objects.all().order_by("-last_name"))


if __name__ == '__main__':
    main()
