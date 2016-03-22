from .models import Film, Review, User
from rest_framework import serializers

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ('title', 'year', 'actors', 'composer', 'director', 'genre')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'date_written', 'heading', 'body', 'rating')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'age', 'user_type', 'location')
