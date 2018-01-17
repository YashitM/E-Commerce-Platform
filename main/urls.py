from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.login, name="login"),
    path('logout/', auth_views.logout, name="logout"),
    path('addToCart/<int:itemID>', views.add_to_cart, name='addToCart'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.index, name="checkout"),
    path('wishlist/', views.index, name="wishlist"),
    path('profile/', views.index, name="profile"),
]