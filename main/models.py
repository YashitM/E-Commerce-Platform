import decimal

from django.contrib.auth.models import User
from django.db import models


class Cart(models.Model):
    item_id = models.IntegerField()
    checked_out = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.FileField()
