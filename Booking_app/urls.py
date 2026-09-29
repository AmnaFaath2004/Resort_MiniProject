from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Booking_app import views, owner_views, custumer_views, admin_views

urlpatterns = [
 # path('',views.Rest_index,name="Rest_index"),
path("dash_board",views.dash_board,name="dash_board"),
 path('Login',views.Login,name='Login'),
 path('',views.listing_resorts,name='listing_resorts'),

 path('logout_view',views.logout_view,name='logout_view'),






 path('owner_Registration',views.owner_Registration,name='owner_Registration'),
 path('User_Registration',views.User_Registration,name='User_Registration'),


 path('owner_dash',owner_views.owner_dash,name='owner_dash'),
 path('profile',owner_views.profile,name='profile'),
 path('Update_profile/<int:id>/',owner_views.Update_profile,name='Update_profile'),
 path('resort',owner_views.resort,name='resort'),
path('view_resort/', owner_views.view_resort, name='view_resort'),
 path('edit_resort/<int:id>/',owner_views.edit_resort,name='edit_resort'),
 path('facilities/<int:resort_id>/',owner_views.facilities,name='facilities'),
 path('edit_facilities/<int:resort_id>/',owner_views.edit_facilities,name='edit_facilities'),
 path('delete_resort/<int:resort_id>/',owner_views.delete_resort,name='delete_resort'),
 path('slot/<int:fec_id>/',owner_views.slot,name='slot'),
 path('view_slot_Owner',owner_views.view_slot_Owner,name='view_slot_Owner'),
 path('delete_slot/<int:id>/',owner_views.delete_slot,name='delete_slot'),



 path('customer_dash',custumer_views.customer_dash,name='customer_dash'),
 path('customer_profile',custumer_views.customer_profile,name='customer_profile'),
 path('update_customer_profile/<int:id>/',custumer_views.update_customer_profile,name='update_customer_profile'),
path('view_slot/<int:resort_id>/',custumer_views.view_slot,name='view_slot'),
path('view_details/<int:id>/',custumer_views.view_details,name='view_details'),
 path('booking',custumer_views.booking,name='booking'),




 path('admin_dash',admin_views.admin_dash,name='admin_dash'),
 path('view_customer',admin_views.customer_list,name='view_customer'),
 path('delete_customer/<int:id>/',admin_views.delete_customer,name='delete_customer'),
 path('update_customer/<int:id>/',admin_views.update_customer,name='update_customer'),

 path('view_owner',admin_views.owner_List,name='view_owner'),
 path('delete_owner/<int:id>/',admin_views.delete_owner,name='delete_owner'),
 path('update_owner/<int:id>/',admin_views.update_owner,name='update_owner')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)