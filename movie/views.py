from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.response import Response


from .models import Movie
from .serializers import MovieSerializer, DetailMovieSerializer


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
    description = "Liste des films"
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    def get(self, request):
        serializer = MovieSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def get_detail(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = DetailMovieSerializer(instance=movie)
        return Response(serializer.data)
