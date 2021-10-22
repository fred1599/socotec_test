from django.db import models
from actor.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    actors = models.ManyToManyField(to=Actor, verbose_name="Acteurs")

    def __str__(self):
        return self.title
