from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.response import Response

from actor.models import Actor

from .models import Movie
from .serializers import MovieSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = "page_size"
    max_page_size = 2
    page_query_param = "p"


class MovieViewSet(viewsets.ViewSet):
    """
    Liste des films
    """

    pagination_class = StandardResultsSetPagination

    def list(self, request):
        self.description = "Liste des films"
        queryset = Movie.objects.all()
        queryset.order_by("title")
        serializer = MovieSerializer(queryset, many=True)
        for entity in serializer.data:
            pks_actors = entity["actors"]
            actors = [str(actor) for actor in Actor.objects.filter(pk__in=pks_actors)]
            entity["actors_names"] = actors
        return Response(serializer.data)
