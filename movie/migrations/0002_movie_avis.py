# Generated by Django 3.2.8 on 2021-10-22 09:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="avis",
            field=models.PositiveIntegerField(
                default=5,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]
