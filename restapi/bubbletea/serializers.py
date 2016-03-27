# Rendering of Python data tyes, model instances and querysets into JSON
from .models import Franchise, Drink, Review, Location
from rest_framework import serializers
from django.contrib.auth.models import User


# Use of hyperlinked model serialisers uses URLs as relationships between models

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
    #Set creator of review and make it read-only to avoid rewrites
    username = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = Review
        fields = ('url', 'franchise_name', 'username', 'date_written', 'heading', 'body', 'rating')
