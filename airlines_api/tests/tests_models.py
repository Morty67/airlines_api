import math

from django.test import TestCase
from airlines_api.models import Aircraft


class AircraftModelTestCase(TestCase):
    def setUp(self):
        self.aircraft = Aircraft.objects.create(
            name="Test Aircraft", identifier=123, seat_capacity=200
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.aircraft), "Aircraft: Test Aircraft with identifier: 123"
        )

    def test_fuel_capacity_calculation(self):
        expected_fuel_capacity = 200 * self.aircraft.identifier
        self.assertEqual(self.aircraft.fuel_capacity, expected_fuel_capacity)

    def test_fuel_consumption_per_minute(self):
        expected_fuel_consumption = round(
            math.log(self.aircraft.identifier) * 0.80, 2
        )
        self.assertEqual(
            self.aircraft.fuel_consumption_per_minute(),
            f"{expected_fuel_consumption} l/min",
        )

    def test_fuel_consumption_with_passengers(self):
        expected_fuel_consumption = round(
            math.log(self.aircraft.identifier) * 0.80, 2
        )
        additional_fuel = 0.002 * self.aircraft.seat_capacity
        total_fuel_consumption = round(
            expected_fuel_consumption + additional_fuel, 2
        )
        self.assertEqual(
            self.aircraft.fuel_consumption_with_passengers(),
            f"{total_fuel_consumption} l/min",
        )
