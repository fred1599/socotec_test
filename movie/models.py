from django.db import models
from actor.models import Actor

from django.db.models import Avg


class Movie(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titre")
    description = models.TextField(verbose_name="Description")
    actors = models.ManyToManyField(to=Actor, verbose_name="Acteurs")

    @property
    def get_average_review(self):
        from review.models import Review

        return Review.objects.filter(movie=self).aggregate(Avg("grade"))

    def __str__(self):
        return self.title
