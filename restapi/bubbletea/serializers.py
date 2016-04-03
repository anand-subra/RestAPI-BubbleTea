# Rendering of Python data tyes, model instances and querysets into JSON
from .models import Franchise, Drink, Review, Location
from rest_framework import serializers
from django.contrib.auth.models import User

# Use of hyperlinked model serialisers uses URLs as relationships between models
class FranchiseSerializer(serializers.HyperlinkedModelSerializer):

    #Return objects associated with franchise instance
    franchise_location = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='location-detail')
    franchise_drink = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='drink-detail')
    franchise_review = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review-detail')

    class Meta:
        model = Franchise
        fields = ('url', 'name', 'style', 'franchise_location', 'franchise_drink', 'franchise_review')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'franchise_location', 'location')

class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drink
        fields = ('url', 'franchise_drink', 'name', 'syrup_type', 'temperature', 'tea_type', 'tea_form', 'topping_type', 'topping_flavour')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    #Set creator of review and make it read-only to avoid rewrites
    username = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = Review
        fields = ('url', 'franchise_review', 'username', 'date_written', 'heading', 'body', 'rating')
