import init_django_orm  # noqa: F401

from db.models import Person


def main():
    records = Person.objects.get(
        last_name="Tesla",
    )
    print(records.delete())


if __name__ == '__main__':
    main()
