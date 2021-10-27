from .models import Movie

from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):

    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = ["title", "description", "actors"]


class DetailMovieSerializer(MovieSerializer):
    class Meta(MovieSerializer.Meta):
        fields = ["title", "description", "actors", "get_average_review"]
