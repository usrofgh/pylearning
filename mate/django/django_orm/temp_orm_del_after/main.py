import init_django_orm  # noqa: F401

from db.models import LiteraryFormat, Book


def main():
    Book.objects.create(title="Gym lifehacks", price=11.7, format_id=2)

if __name__ == '__main__':
    main()
