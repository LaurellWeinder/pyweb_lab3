from decimal import Decimal

from django.db import models



# Create your models here.

class Product(models.Model):

    @property
    def set_price_sale(self):
        return self.price - self.price / 100 * self.discount

    name = models.CharField(max_length=50, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=255)

    class Meta:
        ordering = ['-name'] # This is to fix pagination exception.
