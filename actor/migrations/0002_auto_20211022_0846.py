# Generated by Django 3.2.8 on 2021-10-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("actor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="first_name",
            field=models.CharField(max_length=255, verbose_name="Prénom"),
        ),
        migrations.AlterField(
            model_name="actor",
            name="last_name",
            field=models.CharField(max_length=255, verbose_name="Nom"),
        ),
    ]