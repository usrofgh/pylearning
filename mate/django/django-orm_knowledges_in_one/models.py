from django.db import models

# tables are always in the plural
# In dbs instead of string use varchar and specify max length(necessary) of a string

# why do we need  primary key? - There are two Taras Shevchenko one in 19c
# another 21c, another has written modern. How do we difference them?:
# primary key - INTEGER, NOT NULL, AUTOINCREMENT - it's filling up automatically

# when you add a new column sql-lite full deletes a table and  recreating new with actual columns


class Genders(models.Model):
    GENDERS = (
        ("M", "Male"),
        ("F", "Female"),
        ("A", "Another"),
    )

    gender = models.CharField(
        max_length=1
    )


class Movies(models.Model):
    name = models.CharField(max_length=255, unique=True)
    release_year = models.IntegerField()


class Persons(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.SmallIntegerField(default=None)
    character = models.CharField(max_length=100)
    additional_info = models.CharField(blank=True, max_length=500)

    gender = models.ForeignKey(Genders, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    youtube_link = models.CharField(max_length=500, null=True)
