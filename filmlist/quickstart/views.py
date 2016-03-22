from rest_framework import viewsets
from .models import Film, Review, User
from filmlist.quickstart.serializers import FilmSerializer, ReviewSerializer, UserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows films to be viewed or edited.

    GET api/v1/films/
    """
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows reviews to be viewed or edited.

    GET api/v1/reviews/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows users to be viewed or edited.

    GET api/v1/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
