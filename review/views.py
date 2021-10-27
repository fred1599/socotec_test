from rest_framework import viewsets
from rest_framework.response import Response

from movie.models import Movie

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ViewSet):
    def add_review(self, request, pk):
        """Ajout et notation d'un avis sur un film

        Args:
            name (str): nom du film

        Returns:
            [str]: retourne un json
        """
        self.description = "Ajouter un film"
        review = ReviewSerializer(data=request.data)
        review.is_valid(raise_exception=True)
        data = review.validated_data
        movie = Movie.objects.get(pk=pk)
        Review.objects.create(grade=data["grade"], text=data["text"], movie=movie)
        return Response(
            data
        )  # TODO Créer un sérializer pour informer réponse utilisateur
