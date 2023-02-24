from django.db import models


class LiteraryFormat(models.Model):
    # id will declare automatically
    format = models.CharField(max_length=63, unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Book(models.Model):
    SIZE_BOOK = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.CharField("Just description", max_length=1, choices=SIZE_BOOK, blank=True)

    # CASCADE - delete records from other tables which are related by ForeignKey. It allows to keep data integrity
    # SET_NULL - leaves null values. Also necessary specify null=True as a property
    # Each case need different values in "on_delete", but in most cases you'll use CASCADE
    format = models.ForeignKey(LiteraryFormat, on_delete=models.CASCADE,
                               related_name="books")  # related_name - books_set by default - best practice

    # authors = models.ForeignKey(Author, on_delete=models.CASCADE)  # you need many-to-many here. Cause book can have
    # different authors and each author can be an author of the books
    authors = models.ManyToManyField(Author)  # during a migration creates a binder table "db_book_authors"
    # among authors and books ![](../../relations/many_to_many.png)
    # ![](../../relations/many-to-many_example.png)















# lessons
class Message(models.Model):
    content = models.TextField()
    datetime_field = models.DateTimeField(auto_now=True)


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.name} (age {self.age})"



class Place(models.Model):
    address = models.CharField(max_length=50)
    post_index = models.CharField(max_length=32)


class Caffe(models.Model):
    name = models.CharField(max_length=255)
    place = models.OneToOneField(Place, on_delete=models.CASCADE)
