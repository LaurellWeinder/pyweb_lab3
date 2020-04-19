from decimal import Decimal

from django.db import models



# Create your models here.

class Product(models.Model):
    @staticmethod
    def set_discount(discount) -> Decimal:
        if discount > 0:
            Product.price_sale = Product.price - Product.price / 100 * discount
        return Product.price_sale

    name = models.CharField(max_length=50, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    image = models.CharField(max_length=255)
    price_sale = models.DecimalField(max_digits=10, decimal_places=2, default=set_discount.__get__(object))

