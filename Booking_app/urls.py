from django.urls import path

from Booking_app import views

urlpatterns = [
 path("Rest_index",views.Rest_index,name="Rest_index"),
path("dash_board",views.dash_board,name="dash_board"),
 path('loging',views.loging,name='loging')
]