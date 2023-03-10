from django.db import models


class LiteraryFormat(models.Model):
    format = models.CharField(max_length=63)

    def __str__(self):
        return self.format


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    format = models.ForeignKey(
        LiteraryFormat,
        on_delete=models.CASCADE,
        # related_name="book_set"  # by default
        related_name="books"
    )  # many to one

    # створюється звязуюча таблиця db_book_authors
    # у авторов будет доступ к книгам через rel_name
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return f"{self.title} (price: {self.price}, format: {self.format.format})"


class Car(models.Model):
    MARKET_SEGMENT_CHOICES = (
        ("A", "mini car"),
        ("B", "small car"),
        ("C", "medium car"),
        ("D", "large car"),
        ("F", "luxury car"),
        ("S", "sport car")
    )

    brand = models.CharField(max_length=255)
    horse_power = models.IntegerField()
    creation_date = models.DateField("Use description when it's really necessary", null=True, blank=True)
    description = models.TextField(default="Best ever car")
    market_segment = models.CharField(max_length=1, choices=MARKET_SEGMENT_CHOICES, default="C")

    def __str__(self):
        return f"{self.id}: {self.brand} (power: {self.horse_power})"

class Message(models.Model):
    content = models.TextField()
    datetime_sent = models.DateTimeField(auto_now=True)


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.name} (age: {self.age})"
