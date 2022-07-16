from django.db import models
from rest_framework.exceptions import ValidationError
from zip_airlines import settings
from math import log

# Create your models here.

class Airplane(models.Model):
    airplane_id = models.PositiveIntegerField(unique=True)
    fuel_tank = models.PositiveIntegerField(help_text='Amount of fuel tank')
    consumption = models.FloatField(help_text='Fuel consumption per minute')
    passengers = models.PositiveIntegerField(help_text='Amount of passengers on board')
    minutes_to_fly = models.PositiveIntegerField(help_text='minutes to fly')

    def save(self, *args, **kwargs):
        if Airplane.objects.count() <= settings.MAX_AIRPLANE_COUNT:
            self.fuel_tank = 200 * self.airplane_id
            self.consumption = log(self.airplane_id) * 0.8 + self.passengers * 0.002
            self.minutes_to_fly = self.fuel_tank / self.consumption
            super(Airplane, self).save(*args, **kwargs)
        else:
            raise ValidationError('You cannot add more airplanes')
