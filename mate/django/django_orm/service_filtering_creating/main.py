import init_django_orm  # noqa: F401

from db.models import Book, Author, LiteraryFormat
from services import book as book_service


def main():
    # Author.objects.create(first_name="Joane", last_name="Rowling")
    # Author.objects.create(first_name="John", last_name="Tiffany")
    # Author.objects.create(first_name="Jack", last_name="Thorne")
    # Author.objects.create(first_name="Taras", last_name="Shevchenko")
    # Author.objects.create(first_name="Robert", last_name="Kiyosaki")
    # Author.objects.create(first_name="Sharon", last_name="Lechter")
    # Author.objects.create(first_name="Arthur", last_name="Conan Doyle")
    #
    # LiteraryFormat.objects.create(format="novels")
    # LiteraryFormat.objects.create(format="biography")
    # LiteraryFormat.objects.create(format="mystery")

    # book_service.create_book(
    #     title="Rich dad and Poor dad",
    #     price=11.5,
    #     format_id=2,
    #     authors_ids=[5, 6]
    # )

    print(book_service.get_book(format_id=2, authors_ids=[1, 5]))


if __name__ == '__main__':
    main()
