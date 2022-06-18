from django.db import models
from datetime import datetime
# Create your models here.

class Itinerary(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Event(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length=500)
    googlelink = models.CharField(max_length=1000)
    description = models.CharField(max_length=600)
    itin = models.ManyToManyField(Itinerary)

    formattedtime = " "
    def __str__(self):
        return self.place

class Date(models.Model):
    date = models.DateField()
    events = []