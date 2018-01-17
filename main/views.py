from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from main.models import Item, Cart


def index(request):

    return render(request, 'main/index.html', {"item": Item.objects.all().first()})


def add_to_cart(request, itemID):
    if request.user.cart_set.all().exists():
        cart = request.user.cart_set.get(user_id=request.user.id)
    else:
        cart = Cart()
        cart.user_id = request.user.id
        cart.num_of_items = 0
        cart.total_price = 0.0
        cart.save()
    list_of_item = Item.objects.all()
    for item in list_of_item:
        if item.id == itemID:
            cart.add_item(item)
            # cart.items.add(item)
            # cart.num_of_items += 1
            # cart.total_price += item.unit_price * item.quantity
            break
    return redirect('/')