from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'main/index.html', {"custom_notifications": ""})


def login(request):
    return render(request, 'main/login.html', context=None)
