from django import forms
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from library.settings import AUTH_USER_MODEL


class LiteraryFormat(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(unique=True, max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(upload_to="books/", null=True)

    format = models.ForeignKey(to=LiteraryFormat, on_delete=models.CASCADE)
    authors = models.ManyToManyField(to=AUTH_USER_MODEL)

    class Meta:
        default_related_name = "books"
        ordering = ["title"]

    def __str__(self) -> str:
        return f"{self.title} (price: {self.price}, format: {self.format.name})"


class Author(AbstractUser):
    photo = models.ImageField(null=True)

    class Meta:
        default_related_name = "authors"
        ordering = ["username"]
