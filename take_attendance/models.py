from django.db import models

# Create your models here.

class PrathanaLocation(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the Prathana location")
    latitude = models.CharField(max_length=20, help_text="Latitude of the location")
    longitude = models.CharField(max_length=20, help_text="Longitude of the location")
    start_time = models.TimeField(help_text="Start time for Prathana")
    end_time = models.TimeField(help_text="End time for Prathana")
    radius = models.FloatField(default=100.0, help_text="Maximum allowed distance in meters")

    def __str__(self):
        return self.name
