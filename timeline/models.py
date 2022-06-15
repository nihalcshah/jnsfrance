from django.db import models
from datetime import datetime
# Create your models here.


class Event(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length=500)
    googlelink = models.CharField(max_length=1000)
    description = models.CharField(max_length=600)
    formattedtime = " "
    def __str__(self):
        return self.place

