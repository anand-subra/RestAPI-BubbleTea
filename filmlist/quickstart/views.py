from rest_framework import viewsets
from .models import Franchise, Drink, Review
from filmlist.quickstart.serializers import FranchiseSerializer, DrinkSerializer, ReviewSerializer

class FranchiseViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows shops to be viewed or edited.

    GET api/v1/franchises/
    """
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer

class DrinkViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows drinks to be viewed or edited.

    GET api/v1/drinks/
    """
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows ratings to be viewed or edited.

    GET api/v1/reviews/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
