from .models import Franchise, Drink, Review
from rest_framework import serializers

class FranchiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Franchise
        fields = ('url', 'name', 'style', 'location')

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        # fields = ('id', 'url', 'franchise_name', 'name', 'syrup_type', 'temperature', 'tea_type', 'tea_form', 'topping_type', 'topping_flavour')
        exclude = ['id']

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('url', 'franchise_name','username', 'age', 'date_written', 'heading', 'body', 'rating')

    # Add models of other types
    # e.g. add franchise details within a review:
    #
    # franchise = FranchiseSerializer()
    # fields = ('url', 'franchise', 'username', 'age', 'date_written', 'heading', 'body', 'rating')
