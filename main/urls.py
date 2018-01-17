from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.login, name="login"),
    path('cart/', views.index, name="cart"),
    path('checkout/', views.index, name="checkout"),
    path('wishlist/', views.index, name="wishlist"),
    path('profile/', views.index, name="profile"),
]