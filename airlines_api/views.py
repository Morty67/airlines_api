from rest_framework import viewsets

from airlines_api.models import Aircraft
from airlines_api.serializers import AircraftSerializer


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
