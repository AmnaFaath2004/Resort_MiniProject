from django.contrib import admin

from Booking_app.models import Login, Owner, User

# Register your models here.
admin.site.register(Login)
admin.site.register(Owner)
admin.site.register(User)