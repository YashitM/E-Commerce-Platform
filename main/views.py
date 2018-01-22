from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View

from main.forms import Regform
from main.models import Item, Cart, Category


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


def remove_from_cart(request, itemID):
    Cart.objects.filter(item_id=itemID).delete()
    return redirect('/cart/')


class Register(View):
    form_class = Regform

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if not User.objects.filter(email=email):
                user.set_password(password)
                user.email = email
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('/')
            else:
                return redirect('signup')

        return render(request, 'main/index.html', context=None)


def shop(request):
    items = Item.objects.all()
    return render(request, 'main/shop.html', {'items': items})


def product_details(request, item_id):
    selected_item = get_object_or_404(Item, pk=item_id)
    filtered_items = [item for item in Category.objects.get(name=selected_item.category).item_set.all()[:7] if item.id != selected_item.id]

    return render(request, 'main/product-details.html', {'item': selected_item, 'recommended_items': filtered_items})
