from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_owner=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)

class Owner(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="owner")
    name=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.name

class User(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="user")
    name=models.CharField(max_length=50)
    contact_number=models.CharField(max_length=10)
    email=models.EmailField()
    address=models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Resort(models.Model):
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='resort')
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    picture=models.FileField(upload_to='resort/picture/')
    price=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Facilities(models.Model):
    resort=models.ForeignKey(Resort,on_delete=models.CASCADE,related_name='facilities')
    pool=models.BooleanField(default=False)
    kitchen=models.BooleanField(default=False)
    wifi=models.BooleanField(default=False)
    lawn=models.BooleanField(default=False)
    balcony=models.BooleanField(default=False)

class Slots(models.Model):
    fecility=models.ForeignKey(Facilities,on_delete=models.CASCADE,related_name='facilities')
    from_date=models.DateField()
    to_date=models.DateField()
    slot_status=models.BooleanField(default=0)


class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookings')
    slot=models.ForeignKey(Slots,on_delete=models.CASCADE,related_name='bookings')
    status=models.IntegerField(default=0)
    time_date=models.DateField(auto_now=True)

class Chat(models.Model):
    resort=models.ForeignKey(Resort,on_delete=models.CASCADE,related_name='chats')
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='chats')
    message=models.TextField()
    reply=models.TextField(blank=True,null=True)