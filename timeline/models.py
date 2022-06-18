from django.db import models
from datetime import datetime
# Create your models here.

class Itinerary(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Itinerary'
        verbose_name_plural = 'Itineraries'

    def __str__(self):
        return self.title

class Event(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length=500)
    Travel = models.BooleanField(default=False, help_text="Check if this is a drive or flight")
    hotel = models.BooleanField(default=False, help_text="Check if this is a hotel")
    googlelink = models.CharField(max_length=1000, blank=True, help_text="Link to TripAdvisor or the Hotel (Optional)")
    description = models.CharField(max_length=600, blank=True, help_text="Description of the event (Optional)")
    itin = models.ManyToManyField(Itinerary)

    formattedtime = " "
    def __str__(self):
        return self.place

class Date(models.Model):
    date = models.DateField()
    events = []

    def __str__(self):
        return self.date.strftime("%A, %B %d")