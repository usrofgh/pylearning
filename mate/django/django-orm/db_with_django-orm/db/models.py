from django.db import models


class LiteraryFormat(models.Model):
    # id will declare automatically
    format = models.CharField(max_length=63, unique=True)


class Book(models.Model):
    SIZE_BOOK = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
    )

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField("Just description", max_length=1, choices=SIZE_BOOK, blank=True)


class Message(models.Model):
    content = models.TextField()
    datetime_field = models.DateTimeField()
