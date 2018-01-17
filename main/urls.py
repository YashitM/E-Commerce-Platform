from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index_page"),
    path('login/', views.login, name="login_page"),
    # path('^offerrides/$', views.offer_ride, name="offer_ride"),
    # path('^takerides/$', views.take_ride, name="take_ride"),
    # path('^view_requests/$', views.view_requests, name="view_requests"),
    # path('^profile/$', views.view_profile, name="view_profile"),
    # path('^update_profile/$', views.update_profile, name="update_profile"),
    # path(
    #     '^request_ride/(?P<ride_id>\d+)/$',
    #     views.request_ride,
    #     name="request_ride"),
    # path('^contact_us/$', views.contact_us, name="contact_us"),
    # path(
    #     '^validate_request/(?P<request_id>\d+)/$',
    #     views.validate_ride_request,
    #     name="validate_ride_request"),
    # path('^view_rides/$', views.view_user_rides, name="view_user_rides"),
    # path(
    #     '^cancel_ride/(?P<ride_id>\d+)/$',
    #     views.cancel_ride,
    #     name="cancel_ride"),
    # path('^edit_ride/(?P<ride_id>\d+)/$', views.edit_rides, name="edit_ride"),
]