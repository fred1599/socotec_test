# Generated by Django 3.2.8 on 2021-10-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("actor", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=255, verbose_name="Titre")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "actors",
                    models.ManyToManyField(to="actor.Actor", verbose_name="Acteurs"),
                ),
            ],
        ),
    ]
