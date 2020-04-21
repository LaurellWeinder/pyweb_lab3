from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=255)

    @property
    def set_price_sale(self):
        return self.price - self.price / 100 * self.discount

    def add_to_cart(self, name):
        product = Product.objects.get(name=name)

    class Meta:
        ordering = ['-name']  # This is to fix pagination exception.


class Blog(models.Model):
    heading = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=255)
    icon_chat = models.PositiveIntegerField()

    @property
    def set_pretty_date(self):
        return self.date.strftime('%B %d, %Y')

    class Meta:
        ordering = ['-date']


class CartItem(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
