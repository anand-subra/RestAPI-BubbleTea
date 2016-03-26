from .models import Franchise, Drink, Review, Location
from rest_framework import serializers
from django.contrib.auth.models import User

class FranchiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Franchise
        fields = ('url', 'name', 'style')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'franchise_name', 'location')

class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drink
        fields = ('url', 'franchise_name', 'name', 'syrup_type', 'temperature', 'tea_type', 'tea_form', 'topping_type', 'topping_flavour')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = Review
        fields = ('url', 'franchise_name', 'username', 'age', 'date_written', 'heading', 'body', 'rating')

    # Add models of other types
    # e.g. add franchise details within a review:
    #
    # franchise = FranchiseSerializer()
    # fields = ('url', 'franchise', 'username', 'age', 'date_written', 'heading', 'body', 'rating')
