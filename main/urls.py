from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.index, name="login"),
    path('cart/', views.index, name="cart"),
    path('checkout/', views.index, name="checkout"),
    path('wishlist/', views.index, name="wishlist"),
    path('profile/', views.index, name="profile"),
]