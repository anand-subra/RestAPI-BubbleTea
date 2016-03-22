from .models import Franchise, Drink, Review
from rest_framework import serializers

class FranchiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Franchise
        fields = ('url', 'name', 'style', 'location')

class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'url', 'franchise_name', 'name', 'syrup_type', 'temperature', 'tea_type', 'topping_type', 'topping_flavour')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('url', 'franchise_name', 'username', 'age', 'date_written', 'heading', 'body', 'rating')
