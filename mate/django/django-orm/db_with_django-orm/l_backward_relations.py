import init_django_orm  # noqa F401
from db.models import Book


def main():
    # LiteraryFormat.objects.all().delete()
    # Book.objects.all().delete()
    # Author.objects.all().delete()

    # LiteraryFormat(format="drama").save()
    # LiteraryFormat(format="poetry").save()
    # Author(first_name="Elon", last_name="Musk").save()

    book = Book.objects.get(price=35.82)
    print(book)  # Book object (2)
    print(book.format)  # LiteraryFormat object (19)
    print(book.format.format)  # drama
    print(book.format.books)  # db.Book.None
    print(book.format.books.all()[0].title)  # Future // one-to-many

    # <class 'django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager'>
    print(type(book.format.books))

    # Through Books' field "format" we call LiteraryFormat field "format" - format__format
    print(Book.objects.filter(format__format="drama"))

    # SQL query of this request:
        # SELECT "db_book"."id", "db_book"."title", "db_book"."price", "db_book"."size", "db_book"."format_id", "db_book"."authors_id"
        # FROM "db_book" INNER JOIN "db_literaryformat" ON ("db_book"."format_id" = "db_literaryformat"."id")
        # WHERE "db_literaryformat"."format" = drama
    print(str(Book.objects.filter(format__format="drama").query))




if __name__ == '__main__':
    main()
