from rest_framework import viewsets
from rest_framework.response import Response

from movie.models import Movie

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ViewSet):
    def add_review(self, request):
        """Ajout et notation d'un avis sur un film

        Args:
            name (str): nom du film

        Returns:
            [str]: retourne un json
        """
        error = {
            "status": 400,
            "message": "erreur dans la mise en forme de votre requête",
        }
        name = request.data.get("name")
        self.description = "Ajouter un film"
        review = ReviewSerializer(data=request.data)
        if review.is_valid():
            data = review._validated_data
            movie = Movie.objects.get(title=name)
            Review.objects.get_or_create(
                grade=data["grade"], text=data["text"], movie=movie
            )
            error["status"] = 200
            error["message"] = "Votre avis a bien été enregistré"
        return Response(error)
