from django.urls import path, include
from rest_framework import routers

from airlines_api.views import (
    AircraftViewSet,
    AircraftList,
    TotalInfo,

)

router = routers.DefaultRouter()
router.register("aircraft", AircraftViewSet, basename="aircraft")


urlpatterns = [
    path("", include(router.urls)),
    path("info/", AircraftList.as_view(), name="info-list"),
    path("total/", TotalInfo.as_view(), name="total-info"),

]

app_name = "aircraft"
