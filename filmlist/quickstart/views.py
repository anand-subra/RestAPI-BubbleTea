from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from filmlist.quickstart.permissions import IsOwnerOrReadOnly
from .models import Franchise, Drink, Review, Location
from filmlist.quickstart.serializers import FranchiseSerializer, DrinkSerializer, ReviewSerializer, LocationSerializer

class FranchiseViewSet(viewsets.ModelViewSet):
    # Below is description that is returned
    """
    Endpoint that allows shops to be viewed or edited.

    GET api/v1/franchises/
    """
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly or permissions.IsAdminUser,)

class DrinkViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows drinks to be viewed or edited.

    GET api/v1/drinks/
    """
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly or permissions.IsAdminUser,)

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows ratings to be viewed or edited.

    GET api/v1/reviews/
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class LocationViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows locations to be viewed or edited.

    GET api/v1/locations/
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly or permissions.IsAdminUser,)
