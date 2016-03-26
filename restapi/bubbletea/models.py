# Establishing models for different ways users can use/browse the API
# Importing User model from auth.models for authentication
# Importing validators to validate some input
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Automated primary key generation for franchises
# Return name of franchise when calling object
class Franchise(models.Model):
    name = models.CharField(max_length=20, blank=False)
    style = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


# Automated primary key generation for locations of franchises
# Using foreign key to link many locations to a franchise
class Location(models.Model):
    location = models.CharField(max_length=50, blank=False)
    franchise_name = models.ForeignKey("Franchise", related_name='franchise')


# Automated primary key generation for drinks of franchises
# Using foreign key to link many drinks to a franchise
# Limiting options based on context:
# (i.e. Drinks can only be served hot or cold. Some drinks can be served in either temperature)
# (i.e. drinks can have a fruit-juice-like or milkshake-like form. Some drinks can be in smoothie form, an example of a "special" form)
class Drink(models.Model):
    temperature_choices = ('Cold', 'Hot', 'Hot/Cold')
    tea_type_choices = ('Black', 'Green')
    tea_form_choices = ('Fruit', 'Milk', 'Special')
    franchise_name = models.ForeignKey("Franchise", related_name='franchise')
    name = models.CharField(max_length=50, blank=False)
    syrup_type = models.CharField(max_length=15, blank=False)
    temperature = models.CharField(max_length=8, blank=False, choices=temperature_choices)
    tea_type = models.CharField(max_length=5, blank=False, choices=tea_type_choices)
    tea_form = models.CharField(max_length=7, blank=False, choices=tea_form_choices)
    topping_type = models.CharField(max_length = 15, blank=True)
    topping_flavour = models.CharField(max_length = 25, blank=True)


# Automated primary key generation for reviews of franchises
# Authors (username) of a review is automatically set based on authentication i.e. who is logged in
# timestamp (date_written) is set at time of POST-ing
# Ratings are limited on a scale of 0-10
class Review(models.Model):
    franchise_name = models.ForeignKey("Franchise", related_name='franchise')
    username = models.ForeignKey('auth.User', related_name='reviews')
    age = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(0)], blank=True)
    date_written = models.DateTimeField(auto_now_add=True, blank=False)
    heading = models.CharField(max_length=30, blank=False)
    body = models.CharField(max_length=250, blank=False)
    rating = models.IntegerField(blank=False, validators=[MaxValueValidator(10), MinValueValidator(0)])
