from django.db import models
from actor.models import Actor

from django.core.validators import MinValueValidator, MaxValueValidator


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    actors = models.ManyToManyField(to=Actor, verbose_name="Acteurs")
    avis = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.title
