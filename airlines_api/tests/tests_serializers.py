from django.test import TestCase

from airlines_api.models import Aircraft
from airlines_api.serializers import AircraftSerializer, AircraftListSerializer


class AircraftSerializerTestCase(TestCase):
    def setUp(self):
        self.aircraft_data = {
            "name": "Test Aircraft",
            "identifier": 123,
            "seat_capacity": 200,
        }
        self.aircraft = Aircraft.objects.create(**self.aircraft_data)
        self.serializer = AircraftSerializer(instance=self.aircraft)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            {"id", "name", "identifier", "seat_capacity", "fuel_capacity"},
        )

    def test_serializer_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data["name"], self.aircraft_data["name"])
        self.assertEqual(data["identifier"], self.aircraft_data["identifier"])
        self.assertEqual(
            data["seat_capacity"], self.aircraft_data["seat_capacity"]
        )
        self.assertEqual(data["fuel_capacity"], self.aircraft.fuel_capacity)


class AircraftListSerializerTestCase(TestCase):
    def setUp(self):
        self.aircraft_data = {
            "name": "Test Aircraft",
            "identifier": 123,
            "seat_capacity": 200,
        }
        self.aircraft = Aircraft.objects.create(**self.aircraft_data)
        self.serializer = AircraftListSerializer(instance=self.aircraft)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            {
                "name",
                "fuel_capacity",
                "fuel_consumption",
                "fuel_consumption_with_passengers",
                "flight_duration",
            },
        )

    def test_fuel_consumption_content(self):
        data = self.serializer.data
        expected_fuel_consumption = f"Without passengers: {self.aircraft.fuel_consumption_per_minute()}"
        self.assertEqual(data["fuel_consumption"], expected_fuel_consumption)

    def test_flight_duration_content(self):
        data = self.serializer.data
        fuel_consumption = self.aircraft.fuel_consumption_with_passengers()
        expected_flight_duration = round(
            self.aircraft.fuel_capacity / float(fuel_consumption[:-6]), 2
        )
        self.assertEqual(
            data["flight_duration"], f"{expected_flight_duration} min"
        )

    def test_fuel_consumption_with_passengers_content(self):
        data = self.serializer.data
        expected_fuel_consumption_with_passengers = f"With passengers: {self.aircraft.fuel_consumption_with_passengers()}"
        self.assertEqual(
            data["fuel_consumption_with_passengers"],
            expected_fuel_consumption_with_passengers,
        )
