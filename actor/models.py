from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Prénom")
    last_name = models.CharField(max_length=255, verbose_name="Nom")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
