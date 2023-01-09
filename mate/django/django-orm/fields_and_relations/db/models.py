from django.db import models


# class Car(models.Model):
#     MARKET_SEGMENT_CHOICES = (
#         ("A", "mini car"),
#         ("B", "small car"),
#         ("C", "medium car"),
#         ("D", "large car"),
#         ("F", "luxury car"),
#         ("S", "sport car")
#     )
#
#     brand = models.CharField(
#         "It's a description of this field",  # добавлять только тогда, когда 100% нужны
#         max_length=255
#     )  # python - аттрибут. В БД - поле
#
#     horse_power = models.IntegerField(blank=True)  # blank - пустота, null - надпись null
#     creation_date = models.DateField(null=True)  # после добавления null - мигрируй
#     description = models.TextField(default="Best ever car!")
#
#     market_segment = models.CharField(
#         max_length=1,
#         choices=MARKET_SEGMENT_CHOICES,
#         default="C"  # так как к существующим машинам также нужно добавить значения
#     )
#
#
# class Message(models.Model):
#     content = models.TextField()
#     datetime_sent = models.DateTimeField(auto_now=True)  # чтобы при создании не писать всегда datetime.datetime.now(),
#     # сюда же вписать не вариант это, Так как будет бесконечная миграция из-за обновления времени, поэтому нужно:
#     # auto_now=True
#
#
# class Company(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True)
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()


# class LiteraryFormat(models.Model):
#     format = models.CharField(max_length=255)
#
#
# class Author(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#
#
# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=7, decimal_places=2)  # после запятой 2 цифры
#     format = models.ForeignKey(LiteraryFormat, on_delete=models.CASCADE)  # либо - "LiteraryFormat",
#     authors = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
#     # связь many-to-one/one-to-many построена


class Job(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, blank=True)
    salary = models.DecimalField(max_digits=15, decimal_places=2)


class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    job = models.ForeignKey(Job,
                            on_delete=models.CASCADE,
                            blank=True)
