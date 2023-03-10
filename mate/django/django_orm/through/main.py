import init_django_orm  # noqa: F401

from db.models import Product, Order, OrderItem


def main():
    # iphone = Product.objects.create(
    #     name="Iphone",
    #     price=20_000
    # )
    #
    # ipad = Product.objects.create(
    #     name="Ipad",
    #     price=25_000
    # )
    #
    # mac = Product.objects.create(
    #     name="Macbook",
    #     price=40_000
    # )
    #
    # order1 = Order.objects.create()
    # OrderItem.objects.create(
    #     order=order1,
    #     product=iphone,
    # )
    # OrderItem.objects.create(
    #     order=order1,
    #     product=ipad
    # )
    #
    # order2 = Order.objects.create()
    # OrderItem.objects.create(
    #     order=order2,
    #     product=mac,
    #     amount=10
    # )
    print(Product.objects.filter(name__))


if __name__ == '__main__':
    main()

