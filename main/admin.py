from django.contrib import admin
from .models import Item, Cart, Category

admin.site.register(Cart)
admin.site.register(Item)
admin.site.register(Category)