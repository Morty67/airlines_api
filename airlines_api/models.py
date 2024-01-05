import math

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Aircraft(models.Model):
    name = models.CharField(max_length=50)
    identifier = models.IntegerField(unique=True)
    seat_capacity = models.IntegerField(
        validators=[MinValueValidator(50), MaxValueValidator(500)]
    )
    fuel_capacity = models.IntegerField(default=0)

    def __str__(self):
        return f"Aircraft: {self.name} with identifier: {self.identifier}"

    def save(self, *args, **kwargs):
        self.fuel_capacity = 200 * self.identifier
        super().save(*args, **kwargs)

    def fuel_consumption_per_minute(self):
        fuel_consumption = round(math.log(self.identifier) * 0.80, 2)
        return f"{fuel_consumption} l/min"

    def fuel_consumption_with_passengers(self):
        fuel_consumption = self.fuel_consumption_per_minute()
        seat_capacity = self.seat_capacity
        additional_fuel = 0.002 * seat_capacity
        return (
            f"{round(float(fuel_consumption[:-6]) + additional_fuel, 2)} l/min"
        )
