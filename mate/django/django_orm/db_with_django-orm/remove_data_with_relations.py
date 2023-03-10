import init_django_orm  # noqa: F401


from db.models import LiteraryFormat, Book, Author


def main():
    Book.objects.filter().delete()
    book = Book.objects.create(
        title="Harry Potter and the Cursed Child",
        price=17.5,
        format_id=159
    )

    # book.authors.set([1, 2, 14])  # сразу несколько авторов
    print(book.authors.all())
    book.delete()  # авторы не удалились,
    # книга - да
    # авторы и книги связанные - удалились



if __name__ == '__main__':
    main()
