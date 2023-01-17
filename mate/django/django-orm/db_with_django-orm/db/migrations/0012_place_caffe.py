# Generated by Django 4.1.5 on 2023-01-13 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0011_alter_book_authors_alter_book_format'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('post_index', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Caffe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='db.place')),
            ],
        ),
    ]
