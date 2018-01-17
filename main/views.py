from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from main.models import Item, Cart


def index(request):
    items = Item.objects.all()
    return render(request, 'main/index.html', {"items": items})


def cart(request):
    if request.user.is_authenticated:
        item_ids = Cart.objects.filter(user_id=request.user.id)
        cartItems = [Item.objects.get(pk=i.item_id) for i in item_ids]
        return render(request, 'main/cart.html', {"items_in_cart": cartItems})
    else:
        return redirect('/login/')

def add_to_cart(request, itemID):
    if request.user.is_authenticated:
        cart = Cart()
        cart.user_id = request.user.id
        cart.item_id = Item.objects.get(pk=itemID).id
        cart.save()

        return redirect('/')
    else:
        return redirect('/login/')