# Generated by Django 4.1.7 on 2023-03-06 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='literaryformat',
            name='format',
            field=models.CharField(max_length=63),
        ),
    ]
