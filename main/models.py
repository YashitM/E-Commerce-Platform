from django.db import models


# Create your models here.
class Cart(models.Model):
    num_of_items = models.IntegerField()
    total_price = models.IntegerField()
    checked_out = models.BooleanField(default=False)


class Item(models.Model):
    cart = models.ForeignKey(Cart)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    object_id = models.PositiveIntegerField()

    def total_price(self):
        return self.quantity*self.unit_price
    total_price = property(total_price)

    
