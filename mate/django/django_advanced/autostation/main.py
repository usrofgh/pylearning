import init_django_orm  # noqa: F401

from django.db import transaction

from db.models import Order, Ticket


def create_order(tickets: list[dict]) -> Order:
    with transaction.atomic():
        order = Order.objects.create()

        #  буде створений order вище без даних,. rollback не буде. кошти заплачені.
        #  Треба завернути в tranz
        1 // 0

        for ticket_data in tickets:
            Ticket.objects.create(order=order, **ticket_data)

        return order


if __name__ == '__main__':
    create_order(
        # один тікет з 3 білетами
        tickets=[
            {
                "seat": 10,
                "trip_id": 1,
            },
            {
                "seat": 11,
                "trip_id": 1,
            },
            {
                "seat": 12,
                "trip_id": 1,
            },
        ]
    )
