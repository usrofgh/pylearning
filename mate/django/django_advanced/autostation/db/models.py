from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import UniqueConstraint

import settings


class Bus(models.Model):
    info = models.CharField(max_length=255, null=True)
    num_seats = models.IntegerField()

    class Meta:
        # db_table = "bus"  # change default bus table name
        verbose_name_plural = "buses"  # xz

    def __str__(self):
        return self.info


class Trip(models.Model):
    source = models.CharField(max_length=63)
    destination = models.CharField(max_length=63)
    departure = models.DateTimeField()
    bus = models.ForeignKey("Bus", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.source} - {self.destination} ({self.departure})"

    class Meta:
        indexes = [  # best practice way indexing
            models.Index(fields=["source", "destination"]),  # speed up when look for at the same time with 2 columns
            models.Index(fields=["departure"])  # speed up whe look for only with one this column
        ]


class Ticket(models.Model):
    seat = models.IntegerField()
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trip} - (seat: {self.seat})"

    class Meta:
        constraints = [
            # забороняє мати однакові міста в одному trip
            UniqueConstraint(fields=["seat", "trip"], name="unique_ticket_seat_trip")
        ]

    # не викликається при save, обмеження не спрацює, треба змінити save
    def clean(self):
        if not (1 <= self.seat <= self.trip.bus.num_seats):
            raise ValidationError({
                "seat": f"seat must be in range [1, {self.trip.bus.num_seats}], not {self.seat}"
            })

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.full_clean()  # best practice. Включає в себе clean, validate_unique, clean_fields
        return super(Ticket, self).save(force_insert, force_update, using, update_fields)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey("User", on_delete=models.CASCADE)  #
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # good practice

    class Meta:
        ordering = ["-created_at"]  # сортує від новійшого заказу до старішого

    def __str__(self):
        return str(self.created_at)


# in apps for django's user:
# 'django.contrib.auth',
# 'django.contrib.contenttypes'

# той же функціонал що і у джанго юзера, тільки тут можемо змінити поведінку якщо потрібно
# in settings.py add AUTH_USER_MODEL = "db.User"
# migrates
# python manage.py createsuperuser
class User(AbstractUser):
    pass

# User.objects.all() - bad practice
# get_user_model() - good

# get_user_model().objects.create_user() - for creating users with hash passwords, not just passwd
# john = get_user_model().objects.create_user(username="john_smith", email="john@smith.com", password="johnpassword")
# john.check_password("johnpassword")
# john.set_password("new_passwd")
# john.save()



# trips creating

# import random
# trips = [Trip(
#     source=random.choice(["Kyiv", "Lviv", "Odesa"]),
#     destination=random.choice(["Sofia", "Budapest", "Paris"]),
#     departure="2022-01-01",
#     bus_id=1
# ) for _ in range(1_000_000)]

# res = Trip.objects.bulk_create(trips)
# Trip.objects.create(source="Test indexing", destination="Test destination", departure="2022-01-01", bus_id=1)

# Trip.objects.filter(source="Test indexing") 0.078991s
# after indexing  0.001000s
