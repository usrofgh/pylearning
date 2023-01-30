# Generated by Django 4.1.5 on 2023-01-10 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('release_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.SmallIntegerField(default=None)),
                ('character', models.CharField(max_length=100)),
                ('additional_info', models.CharField(blank=True, max_length=500)),
                ('youtube_link', models.CharField(max_length=500, null=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.genders')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.movies')),
            ],
        ),
    ]