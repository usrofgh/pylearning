# Generated by Django 4.1.7 on 2023-03-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0010_alter_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
