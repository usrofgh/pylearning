# Generated by Django 4.1.7 on 2023-03-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='creation_date',
            field=models.DateField(null=True),
        ),
    ]
