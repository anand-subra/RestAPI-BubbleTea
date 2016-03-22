from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Film(models.Model):
    title = models.CharField(max_length=100, primary_key=True, blank=False)
    year = models.IntegerField(blank=False, validators=[MaxValueValidator(3000), MinValueValidator(1850)])
    actors = models.CharField(max_length=200, blank=True)
    composer = models.CharField(max_length=40, blank=True)
    director = models.CharField(max_length=40, blank=True)
    genre = models.CharField(max_length=15, blank=True)

class Review(models.Model):
    date_written = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=30, blank=False)
    body = models.CharField(max_length=250, blank=False)
    rating = models.IntegerField(blank=True, validators=[MaxValueValidator(10), MinValueValidator(0)])

class User(models.Model):
    username = models.CharField(max_length=40, primary_key=True,blank=False)
    age = models.IntegerField(validators=[MaxValueValidator(150), MinValueValidator(0)], blank=False)
    user_type = models.CharField(max_length=15, blank=False)
    location = models.CharField(max_length = 25, blank=True)
