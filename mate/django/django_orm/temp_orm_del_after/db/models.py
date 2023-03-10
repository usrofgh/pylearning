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
        related_name="books"
    )
    authors = models.ManyToManyField(Author, related_name="books")

    def __str__(self):
        return f"{self.title} (price: {self.price}, format: {self.format.format})"


class Car(models.Model):
    SEGMENTS = [
        ("S", "Small car"),
        ("M", "Medium car"),
        ("L", "Large car"),
    ]
    brand = models.CharField(max_length=255)
    horse_power = models.IntegerField()
    creation_date = models.DateField(null=True)
    description = models.TextField()
    market_segment = models.CharField(
        max_length=1,
        choices=SEGMENTS,
        default="M",
    )

    def __str__(self) -> str:
        return f"{self.id} {self.brand} (power: {self.horse_power})"
