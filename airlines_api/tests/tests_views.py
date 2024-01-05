from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from airlines_api.models import Aircraft


class AircraftViewSetTestCase(APITestCase):
    def setUp(self):
        self.aircraft_data = {
            "name": "Test Aircraft",
            "identifier": 123,
            "seat_capacity": 200,
        }
        self.aircraft = Aircraft.objects.create(**self.aircraft_data)
        self.url = reverse("aircraft:aircraft-list")

    def test_get_aircraft_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.aircraft_data["name"])

    def test_create_aircraft(self):
        new_aircraft_data = {
            "name": "New Aircraft",
            "identifier": 456,
            "seat_capacity": 300,
        }
        response = self.client.post(self.url, data=new_aircraft_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Aircraft.objects.count(), 2)
        self.assertEqual(
            Aircraft.objects.last().name, new_aircraft_data["name"]
        )
