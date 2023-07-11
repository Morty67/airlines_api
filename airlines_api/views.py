import math

from django.db.models import Sum
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from airlines_api.models import Aircraft
from airlines_api.serializers import (
    AircraftSerializer,
    AircraftListSerializer,
)


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer


class AircraftList(APIView):
    def get(self, request):
        aircraft_list = Aircraft.objects.all()
        serializer = AircraftListSerializer(aircraft_list, many=True)
        return Response(serializer.data)


class TotalInfo(APIView):
    def get(self, request):
        aircrafts = Aircraft.objects.all()

        total_flight_duration = sum(
            float(entry["flight_duration"][:-4])
            for entry in AircraftListSerializer(aircrafts, many=True).data
        )

        total_fuel_consumption = sum(
            float(entry["fuel_consumption_with_passengers"][16:-6])
            for entry in AircraftListSerializer(aircrafts, many=True).data
        )

        total_fuel_consumption_with_passengers = (
            total_fuel_consumption * total_flight_duration
        )

        result = {
            "total_flight_duration_in_minutes": round(
                total_flight_duration, 2
            ),
            "total_fuel_consumption_with_passengers_in_litres": round(
                total_fuel_consumption_with_passengers, 2
            ),
        }

        return Response(result)
