from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

from movie.models import Movie


class Review(models.Model):
    grade = models.PositiveIntegerField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    movie = models.OneToOneField(to=Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie} - moyenne {self.grade}"
