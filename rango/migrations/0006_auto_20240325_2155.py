# Generated by Django 2.1.5 on 2024-03-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20240325_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
