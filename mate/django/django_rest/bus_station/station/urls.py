from django.urls import path, include

from station.serializers import TripSerializer
# from station.views import bus_list, bus_detail
from station.views import (
    BusList,
    BusDetail,
    BusListWithoutAPI,
    BusDetailWithoutAPI,
    BusListWithListCreate,
    BusDetailWith,
    BusViewSet, BusViewSetAutomaticallyAddedMixins, TripViewSet, FacilityViewSet, OrderView
)


# bus_list = BusViewSet.as_view(actions={"get": "list", "post": "create"})
# bus_detail = BusViewSet.as_view(actions={
#     "get": "retrieve",
#     "put": "update",
#     "patch": "partial_update",
#      "delete": "destroy"
# })
#
# urlpatterns = [
#     # path("buses/", BusListWithoutAPI.as_view(), name="bus-list"),
#     # path("buses/<int:pk>/", BusDetailWithoutAPI.as_view(), name="bus-detail"),
#
#     # path("buses/", BusList.as_view(), name="bus-list"),
#     # path("buses/<int:pk>/", BusDetail.as_view(), name="bus-detail"),
#
#     # path("buses/", BusListWithListCreate.as_view(), name="bus-list"),
#     # path("buses/<int:pk>/", BusDetailWith.as_view(), name="bus-detail"),
#
#     path("buses/", bus_list, name="bus-list"),
#     path("buses/<int:pk>/", bus_detail, name="bus-detail")
# ]




# не красиво виглядає, краще юзати routers
from rest_framework import routers

router = routers.DefaultRouter()
router.register("buses", BusViewSetAutomaticallyAddedMixins)
router.register("trips", TripViewSet)
router.register("facilities", FacilityViewSet)
router.register("orders", OrderView)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "station"
