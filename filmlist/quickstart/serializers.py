from .models import Film, Review, User
from rest_framework import serializers

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ('url', 'title', 'year', 'actors', 'composer', 'director', 'genre')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('url', 'id', 'date_written', 'heading', 'body', 'rating', 'film_name', 'user_name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'age', 'user_type', 'location')
