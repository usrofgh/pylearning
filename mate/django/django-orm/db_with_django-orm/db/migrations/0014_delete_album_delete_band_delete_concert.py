# Generated by Django 4.1.5 on 2023-01-14 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0013_album_band_concert'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Band',
        ),
        migrations.DeleteModel(
            name='Concert',
        ),
    ]