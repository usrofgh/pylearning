from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(
        Product,
        related_name="orders",
        through="OrderItem"
    )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
