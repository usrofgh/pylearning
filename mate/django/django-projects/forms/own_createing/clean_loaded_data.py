import init_django_orm  # noqa: F401

from catalog.models import LiteraryFormat, Author, Book


def clean():
    LiteraryFormat.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()


if __name__ == '__main__':
    clean()
