from django.contrib.auth.models import User
from django.db import models


class Cart(models.Model):
    num_of_items = models.IntegerField()
    total_price = models.IntegerField()
    checked_out = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.FileField()


    def total_price(self):
        return self.quantity*self.unit_price
    total_price = property(total_price)



