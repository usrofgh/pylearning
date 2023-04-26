import os.path
import uuid

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint
from django.utils.text import slugify

from app import settings


class Facility(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        verbose_name_plural = "facilities"

    def __str__(self):
        return self.name


def bus_image_file_path(instance, filename: str):
    extension = filename.rsplit(".")[1]
    filename = f"{slugify(instance.info)}-{uuid.uuid4()}.{extension}"

    return os.path.join("uploads/buses/", filename)  # difference OS - different working


class Bus(models.Model):
    info = models.CharField(max_length=255, null=True)
    num_seats = models.IntegerField()
    facilities = models.ManyToManyField(to=Facility)
    image = models.ImageField(null=True, upload_to=bus_image_file_path)  # TODO: upload_to correct pass

    class Meta:
        verbose_name_plural = "buses"
        default_related_name = "buses"

    @property
    def is_mini(self):
        return self.num_seats < 10

    def __str__(self):
        return str(self.info)


class Trip(models.Model):
    source = models.CharField(max_length=63)
    destination = models.CharField(max_length=63)
    departure = models.DateTimeField()
    bus = models.ForeignKey(to=Bus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source} - {self.destination} ({self.departure})"

    class Meta:
        default_related_name = "trips"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # good practice

    class Meta:
        default_related_name = "orders"
        ordering = ["-created_at"]  # сортує від новійшого заказу до старішого

    def __str__(self):
        return str(self.created_at)


class Ticket(models.Model):
    seat = models.IntegerField()
    trip = models.ForeignKey(to=Trip, on_delete=models.CASCADE)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trip} - (seat: {self.seat})"

    class Meta:
        default_related_name = "tickets"
        ordering = ("seat",)
        constraints = [
            UniqueConstraint(fields=["seat", "trip"], name="unique_ticket_seat_trip")
        ]

    @staticmethod
    def validate_seat(seat: int, num_seats: int, error_to_raise):
        if not (1 <= seat <= num_seats):
            raise error_to_raise({
                "seat": f"seat must be in range [1, {num_seats}], not {seat}"
            })

    # не викликається при save, обмеження не спрацює, треба змінити save
    def clean(self):
        Ticket.validate_seat(self.seat, self.trip.bus.num_seats, ValidationError)
        # if not (1 <= self.seat <= self.trip.bus.num_seats):
        #     raise ValidationError({
        #         "seat": f"seat must be in range [1, {self.trip.bus.num_seats}], not {self.seat}"
        #     })  - moved to validate_seat, cause dublicate of login in serializers


    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.full_clean()  # best practice. Включає в себе clean, validate_unique, clean_fields
        return super(Ticket, self).save(force_insert, force_update, using, update_fields)
