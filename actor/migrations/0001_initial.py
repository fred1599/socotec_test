# Generated by Django 3.2.8 on 2021-10-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255, verbose_name="Prénom")),
                ("last_name", models.CharField(max_length=255, verbose_name="Nom")),
            ],
        ),
    ]
