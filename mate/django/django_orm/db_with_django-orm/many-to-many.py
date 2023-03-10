import init_django_orm  # noqa: F401

from db.models import (
    LiteraryFormat, Car, Message, Company,
    Person, Book, Author)


def main():
    # book = Book.objects.last()
    # print(book.authors.all())  # автора книги
    # author = Author.objects.first()
    # # print(book.authors.all().get(last_name="pew").last_name)
    # livesey = Author.objects.get(first_name="doctor")
    # print(livesey.books.all())  # книги автора
    #
    # # sharon = Author.objects.create(first_name="Sharon", last_name="Lencher")
    # # island = Book.objects.get(title="island")
    # # print(island.authors.add(sharon))
    #
    # # below same only via instances
    #
    # lit_format = LiteraryFormat.objects.first()
    # sherlok_book = Book(title="Sherlok Homes", price=22.5, format=lit_format)
    # arthur = Author(first_name="Arthur", last_name="Conan")
    #
    # sherlok_book.save()
    # # sherlok_book.authors.add(arthur)  # we didn't save author
    # arthur.save()
    # sherlok_book.authors.add(arthur)

    book = Book.objects.last()
    # book.authors.add(1, 2, 3)
    book.authors.set([1])  # delete others and keep only 1
    # при m-t-m не делается каскадное удаление



if __name__ == '__main__':
    main()
