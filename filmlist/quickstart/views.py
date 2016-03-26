# Import viewsets, permissions, models and serializers
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
    # View returns all objects
    queryset = Franchise.objects.all()
    serializer_class = FranchiseSerializer

    # Only admin users have unrestricted access to object(s), other users have read-only access
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly or permissions.IsAdminUser,)

    # Queries can be made and returned by entering parameters into the URL, filtering objects accordingly
    # e.g. http://.../api/v1/franchises?name=T4
    def get_queryset(self):
        qs = Franchise.objects.all()
        searchName = self.request.query_params.get('name', None)
        searchStyle = self.request.query_params.get('style', None)
        if searchName is not None:
            qs = qs.filter(name=searchName)
        if searchStyle is not None:
            qs = qs.filter(style=searchStyle)
        return qs

class DrinkViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows drinks to be viewed or edited.

    GET api/v1/drinks/
    """
    # View returns all objects
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

    # Only admin users have unrestricted access to object(s), other users have read-only access
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly or permissions.IsAdminUser,)

    # Queries can be made and returned by entering parameters into the URL, filtering objects accordingly
    # e.g. http://.../api/v1/drinks?tea_type=Green
    def get_queryset(self):
        qs = Drink.objects.all()
        searchName = self.request.query_params.get('name', None)
        searchTemperature = self.request.query_params.get('temperature', None)
        searchTeaType = self.request.query_params.get('tea_type', None)
        searchTeaForm = self.request.query_params.get('tea_form', None)
        searchFranchiseName = self.request.query_params.get('franchise_name', None)
        if searchName is not None:
            qs = qs.filter(name=searchName)
        if searchTemperature is not None:
            qs = qs.filter(temperature=searchTemperature)
        if searchTeaType is not None:
            qs = qs.filter(tea_type=searchTeaType)
        if searchTeaForm is not None:
            qs = qs.filter(tea_form=searchTeaForm)
        if searchFranchiseName is not None:
            qs = qs.filter(franchise_name=searchFranchiseName)
        return qs

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows ratings to be viewed or edited.

    GET api/v1/reviews/
    """
    # View returns all objects
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Only owner has unrestricted access to their object(s), authenticaed users can create object(s), other users have read-only access
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # Queries can be made and returned by entering parameters into the URL, filtering objects accordingly
    # e.g. http://.../api/v1/reviews?franchise_name=T4
    def get_queryset(self):
        qs = Review.objects.all()
        searchUsername = self.request.query_params.get('username', None)
        searchFranchiseName = self.request.query_params.get('franchise_name', None)
        searchRating = self.request.query_params.get('rating', None)
        if searchUsername is not None:
            qs = qs.filter(username=searchUsername)
        if searchFranchiseName is not None:
            qs = qs.filter(franchise_name=searchFranchiseName)
        if searchRating is not None:
            qs = qs.filter(rating=searchRating)
        return qs

    # On instantiating the object, pass through the author of the review (logged-in user)
    def perform_create(self, serializer):
        serializer.save(username=self.request.user)

class LocationViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows locations to be viewed or edited.

    GET api/v1/locations/
    """
    # View returns all objects
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    # Only admin users have unrestricted access to object(s), other users have read-only access
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly or permissions.IsAdminUser,)

    # Queries can be made and returned by entering parameters into the URL, filtering objects accordingly
    # e.g. http://.../api/v1/locations?franchise_name=T4
    def get_queryset(self):
        qs = Location.objects.all()
        searchFranchiseName = self.request.query_params.get('franchise_name', None)
        if searchFranchiseName is not None:
            qs = qs.filter(franchise_name=searchFranchiseName)
        return qs
