from django.db import transaction
from django.db.models import UniqueConstraint
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from station.models import Bus, Trip, Facility, Ticket, Order


class BusSerializerBase(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    info = serializers.CharField(required=False)
    num_seats = serializers.IntegerField(required=True)

    # validated_data - зберігає info, num_seats
    def create(self, validated_data):
        return Bus.objects.create(**validated_data)

    def update(self, instance: Bus, validated_data):
        # оновляємо якщо є значеня, якщо ні - залишаємо старе
        instance.info = validated_data.get("info", instance.info)
        instance.num_seats = validated_data.get("num_seats", instance.num_seats)
        instance.save()
        return instance


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"


class FacilityListSerializer(FacilitySerializer):
    class Meta:
        model = Facility
        fields = ("name",)


class FacilityDetailSerializer(FacilitySerializer):
    class Meta:
        model = Facility
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ("id", "info", "num_seats", "is_mini", "facilities")


class BusListSerializer(BusSerializer):
    facilities = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")


class BusDetailSerializer(BusSerializer):
    facilities = FacilitySerializer(many=True, read_only=True)


class BusImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ("id", "image")


class TripSerializer(serializers.ModelSerializer):
    # bus = BusSerializer(many=False)  # cause 1 trip has only 1 bus - doesn't work, we don't want to create new bus
    # and read_only doesn't help too - cause we won't be able to fill this field, solution - create new serializer
    class Meta:
        model = Trip
        fields = "__all__"


class TripListSerializer(TripSerializer):
    # bus = BusSerializer(many=False, read_only=True)  # no custom
    bus_num_seats = serializers.IntegerField(source="bus.num_seats", read_only=True)
    bus_info = serializers.CharField(source="bus.info", read_only=True)
    tickets_available = serializers.IntegerField(read_only=True)

    class Meta:
        model = Trip
        fields = (
            "id", "source",
            "destination", "departure",
            "bus_info", "bus_num_seats",
            "tickets_available"
        )


class TicketSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs)
        Ticket.validate_seat(attrs["seat"], attrs["trip"].bus.num_seats, serializers.ValidationError)
        # if not (1 <= attrs["seat"] <= attrs["trip"].bus.num_seats):
        #     raise serializers.ValidationError({
        #         "seat": f"seat must be in range [1, {attrs['trip'].bus.num_seats}], not {attrs['seat']}"
        #     })

        return data

    class Meta:
        model = Ticket
        fields = ("id", "seat", "trip")
        validators = [
            UniqueTogetherValidator(queryset=Ticket.objects.all(), fields=["seat", "trip"])
        ]


class TripDetailSerializer(TripSerializer):
    bus = BusDetailSerializer(many=False, read_only=True)
    # tickets = TicketSeatSerializer(many=True, read_only=True)
    # or
    taken_seats = serializers.SlugRelatedField(
        source="tickets",
        many=True,
        read_only=True,
        slug_field="seat"
    )

    class Meta:
        model = Trip
        fields = ("id", "source", "destination", "departure", "bus", "taken_seats")


# class TicketSeatSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Ticket
#         fields = ("seat",)


class TicketListSerializer(TicketSerializer):
    trip = TripListSerializer(many=False, read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=False, allow_empty=False)

    class Meta:
        model = Order
        fields = ("id", "tickets", "created_at")  # tickets - backward relations

    @transaction.atomic
    def create(self, validated_data):
        tickets_data = validated_data.pop("tickets")
        order = Order.objects.create(**validated_data)
        for ticket_data in tickets_data:
            Ticket.objects.create(order=order, **ticket_data)
        return order


class OrderListSerializer(OrderSerializer):
    tickets = TicketListSerializer(many=True, read_only=True)
