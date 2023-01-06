from django.db import models


# за запись модели в БД отвечают "миграции" - отвечают за изменения схемы в БД
# создаю 1-ю миграцию где будет таблиц класса, с id и форматом:

class LiteraryFormat(models.Model):
    # id = models.BigAutoField(primary_key=True)  # необязательно, под капотом автоматически это вставляет
    format = models.CharField(max_length=63)
