from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Franchise(models.Model):
    name = models.CharField(max_length=20, blank=False)
    style = models.CharField(max_length=20, blank=False)
    # location = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Location(models.Model):
    location = models.CharField(max_length=50, blank=False)
    franchise_name = models.ForeignKey("Franchise", related_name='franchise')


class Drink(models.Model):
    temperature_choices = ('Cold', 'Hot', 'Hot/Cold')
    tea_type_choices = ('Black', 'Green')
    tea_form_choices = ('Fruit', 'Milk', 'Special')
    franchise_name = models.ForeignKey("Franchise", related_name='franchise')
    name = models.CharField(max_length=50, blank=False)
    syrup_type = models.CharField(max_length=15, blank=True)
    temperature = models.CharField(max_length=8, blank=False, choices=temperature_choices)
    tea_type = models.CharField(max_length=5, blank=False, choices=tea_type_choices)
    tea_form = models.CharField(max_length=7, blank=False, choices=tea_form_choices)
    topping_type = models.CharField(max_length = 15, blank=False)
    topping_flavour = models.CharField(max_length = 25, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    franchise_name = models.ForeignKey("Franchise", related_name='franchise')
    username = models.ForeignKey('auth.User', related_name='reviews')
    age = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(0)], blank=False)
    date_written = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=30, blank=False)
    body = models.CharField(max_length=250, blank=False)
    rating = models.IntegerField(blank=True, validators=[MaxValueValidator(10), MinValueValidator(0)])
