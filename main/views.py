from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View

from main.forms import Regform
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


class Register(View):
    form_class = Regform

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'main/signup.html', {'form': form})

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
