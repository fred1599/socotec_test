from django.db import models

from movie.models import Movie


class Review(models.Model):
    grade = models.CharField(max_length=20)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE)
