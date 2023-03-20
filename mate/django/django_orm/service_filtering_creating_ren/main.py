import init_django_orm  # noqa: F401

from services import book as book_service


def main():
    print(book_service.get_books(
        format_id=2,
        authors_ids=[5, 6]
    ))


if __name__ == '__main__':
    main()
