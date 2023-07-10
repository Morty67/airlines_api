from rest_framework import serializers

from airlines_api.models import Aircraft


class AircraftSerializer(serializers.ModelSerializer):
    fuel_capacity = serializers.ReadOnlyField()

    class Meta:
        model = Aircraft
        fields = ["name", "identifier", "seat_capacity", "fuel_capacity"]
