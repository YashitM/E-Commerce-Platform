from django.db import models

# Create your models here.
class Cart(models.Model):
    num_of_items = models.IntegerField()
    total_price = models.IntegerField()