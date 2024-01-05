from rest_framework import serializers

from airlines_api.models import Aircraft


class AircraftSerializer(serializers.ModelSerializer):
    fuel_capacity = serializers.ReadOnlyField()

    class Meta:
        model = Aircraft
        fields = ["id", "name", "identifier", "seat_capacity", "fuel_capacity"]


class AircraftListSerializer(serializers.ModelSerializer):
    fuel_consumption = serializers.SerializerMethodField()
    flight_duration = serializers.SerializerMethodField()
    fuel_consumption_with_passengers = serializers.SerializerMethodField()

    class Meta:
        model = Aircraft
        fields = [
            "name",
            "fuel_capacity",
            "fuel_consumption",
            "fuel_consumption_with_passengers",
            "flight_duration",
        ]

    def get_fuel_consumption(self, aircraft):
        return f"Without passengers: {aircraft.fuel_consumption_per_minute()}"

    def get_flight_duration(self, aircraft):
        fuel_consumption = aircraft.fuel_consumption_with_passengers()
        return (
            f"{round(aircraft.fuel_capacity / float(fuel_consumption[:-6]), 2)} min"
                )

    def get_fuel_consumption_with_passengers(self, aircraft):
        return (
            f"With passengers: {aircraft.fuel_consumption_with_passengers()}"
        )
