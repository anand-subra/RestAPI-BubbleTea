from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Film(models.Model):

    name = models.CharField(max_length=100, unique=True, blank=False)
    year = models.IntegerField(blank=False, validators=[MaxValueValidator(3000), MinValueValidator(1850)])
    rating = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(0)])
