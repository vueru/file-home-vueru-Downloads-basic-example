from __future__ import unicode_literals
from django.db import models
from multiselectfield import MultiSelectField

class Beer(models.Model):
    BEER_CHOICES = (
        ('FIRST', 'first'),('second', 'second'),
    )
    title = MultiSelectField(choices = BEER_CHOICES)



# Create your models here.
