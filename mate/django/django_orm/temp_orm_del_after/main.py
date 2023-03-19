import init_django_orm  # noqa: F401

from db.models import LiteraryFormat, Book, Car


def main():
    # Book.objects.create(title="Gym lifehacks", price=11.7, format_id=2)
    print(Car.objects.filter(creation_date__year=2019))
if __name__ == '__main__':
    main()
