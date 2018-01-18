from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', auth_views.login, name="login"),
    path('signup/', views.Register.as_view() , name="signup"),
    path('logout/', auth_views.logout, name="logout"),
    path('addToCart/<int:itemID>', views.add_to_cart, name='addToCart'),
    path('removeFromCart/<int:itemID>', views.remove_from_cart, name='removeFromCart'),
    path('item/<int:item_id>', views.product_details, name='product_details'),
    path('cart/', views.cart, name="cart"),
    path('shop/', views.shop, name="shop"),
    path('checkout/', views.index, name="checkout"),
    path('wishlist/', views.index, name="wishlist"),
    path('profile/', views.index, name="profile"),
]