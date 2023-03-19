from django.db import models


class BankAccount(models.Model):
    owner = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.owner}: {self.amount}"
