from django.db import transaction

import init_django_orm  # noqa: F401

from db.models import BankAccount


def main():
    bob = BankAccount.objects.get(owner="Bob")
    alice = BankAccount.objects.get(owner="Alice")

    transfer(bob, alice, 200)


def transfer(from_: BankAccount, to: BankAccount, amount: int):
    from_.amount -= amount
    to.amount += amount

    with transaction.atomic():
        from_.save()
        1 // 0  # rollback here
        to.save()

    # from_.save()
    # 1 // 0  # turn off electricity  # кошти відправлені, з балансу зняті - збережено, а ось поповнення - ні
    # # помилка зробила дані неконсинстентними - загальна сума тепер != тій що була перед переказом
    # # для рішення потрібно додати атомарну транзакцію
    # to.save()


if __name__ == '__main__':
    main()
