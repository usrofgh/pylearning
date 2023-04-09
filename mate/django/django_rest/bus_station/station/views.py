from django.db.models import Count, F
from rest_framework import status, mixins, generics, viewsets, views
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from station.models import Bus, Trip, Facility, Order
from station.serializers import BusSerializer, TripSerializer, TripListSerializer, FacilitySerializer, \
    BusDetailSerializer, BusListSerializer, TripDetailSerializer, FacilityListSerializer, FacilityDetailSerializer, \
    OrderSerializer, OrderListSerializer


# function-based виконує не одну задачу а багато - post/get - віддільно. Юзаємо class-based views(APIViews)
# APIView юзати коли кастомні дії, якщо CRUD(базове) -  generics.GenericAPIViews котрий маэ CRUD
#-----------------------------------------------------------------------------------------------------------------------
@api_view(["GET", "POST"])  # робить такі речі як JsonParser, JsonResponse
def bus_list(request):
    if request.method == "GET":
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        # return JsonResponse(serializer.data, status=200, safe=False)
        return Response(serializer.data, status=200)

    if request.method == "POST":
        # вписываем data - создаем новый, не вписываем - читаем старый
        serializer = BusSerializer(data=request.data)  # pydict, за нас преобразуется с помощью api_view
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST", "DELETE"])
def bus_detail(request, pk):
    bus = get_object_or_404(Bus, pk=pk)

    if request.method == "GET":
        serializer = BusSerializer(bus)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = BusSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#-----------------------------------------------------------------------------------------------------------------------
class BusListWithoutAPI(APIView):
    def get(self, request):
        buses = Bus.objects.all()
        serializer = BusSerializer(buses, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusDetailWithoutAPI(APIView):
    def get_object(self, pk):
        return get_object_or_404(Bus, pk=pk)

    def get(self, request, pk):
        bus = self.get_object(pk)
        serializer = BusSerializer(bus)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        bus = self.get_object(pk)
        serializer = BusSerializer(bus, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-----------------------------------------------------------------------------------------------------------------------

class BusList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    # як бачимо метод загальний, Тому можна його винести
    # def get(self, request):
    #     queryset = self.queryset()
    #     serializer = self.get_serializer_class()(queryset, many=True)
    #     return Response(serializer.data, status=200)

    # def post(self, request):
    #     serializer = BusSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BusDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

    # def get_object(self, pk):
    #      return get_object_or_404(Bus, pk=pk)
    #
    # def get(self, request, pk):
    #     bus = self.get_object(pk)
    #     serializer = BusSerializer(bus)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def put(self, request, pk):
    #     bus = self.get_object(pk)
    #     serializer = BusSerializer(bus, data=request.data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, pk):
    #     bus = self.get_object(pk)
    #     bus.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#-----------------------------------------------------------------------------------------------------------------------

# Далі можна юзати ListCreateAPIView, він має в собі вже готові get/post
# це перший підхід
class BusListWithListCreate(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class BusDetailWith(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer

#-----------------------------------------------------------------------------------------------------------------------

# другий підхід, щоб поєднати 2 класи
class BusViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
#-----------------------------------------------------------------------------------------------------------------------
class BusViewSetAutomaticallyAddedMixins(viewsets.ModelViewSet):
    queryset = Bus.objects.prefetch_related("facilities")
    serializer_class = BusSerializer

    @staticmethod
    def _params_to_ints(qs):
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        queryset = self.queryset
        facilities = self.request.query_params.get("facilities")

        if facilities:
            facilities_ids = self._params_to_ints(facilities)
            queryset = queryset.filter(facilities__id__in=facilities_ids)

        return queryset.distrinct()

    def get_serializer_class(self):
        if self.action == "list":
            return BusListSerializer
        if self.action == "retrieve":
            return BusDetailSerializer
        return BusSerializer

#-----------------------------------------------------------------------------------------------------------------------


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            queryset = (
                queryset
                .select_related("bus")
                .annotate(tickets_available=F("bus__num_seats") - Count("tickets"))
            ).order_by("id")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return TripListSerializer
        if self.action == "retrieve":
            return TripDetailSerializer
        return TripSerializer


class FacilityViewSet(viewsets.ModelViewSet):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer

    def get_serializer_class(self):
        if self.action == "list":
            return FacilityListSerializer
        if self.action == "retrieve":
            return FacilityDetailSerializer
        return FacilitySerializer


class OrderPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = OrderPagination

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)

        if self.action == "list":
            queryset = queryset.prefetch_related("tickets__trip__bus")

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return OrderListSerializer
        return OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
