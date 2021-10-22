import json

from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie

PAGINATION_BY = 5


@api_view(["GET"])
def get_page_movie(request, n):
    """retourne tous les films de la page n

    Args:
        n (int): numéro de la page
    """

    movies_list = Movie.objects.values_list("title")
    number_of_movies = 0

    if movies_list:
        movies = [v[0] for v in movies_list]
        number_of_movies = len(movies)

    pages = (number_of_movies // PAGINATION_BY) + 1

    if movies:
        movies_for_page = movies[n - 1 : (n - 1 + PAGINATION_BY)]

    data = {
        "nombre de pages": pages,
        "nombre de films": number_of_movies,
        "page": n,
        "films": movies_for_page,
    }

    return Response(json.dumps(data, ensure_ascii=False), status=status.HTTP_200_OK)
