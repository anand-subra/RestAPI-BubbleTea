from rest_framework import viewsets
from .models import Film, Review, User
from filmlist.quickstart.serializers import FilmSerializer, ReviewSerializer, UserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows films to be viewed or edited.

    GET /films/
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.

    GET /reviews/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.

    GET /users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
