from django.urls import path, include
from rest_framework import routers

from airlines_api.views import (
    AircraftViewSet,

)

router = routers.DefaultRouter()
router.register("aircraft", AircraftViewSet, basename="aircraft")


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "aircraft"
