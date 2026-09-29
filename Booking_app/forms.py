from django import forms
from django.contrib.auth.forms import UserCreationForm

from Booking_app.models import Login, Owner, User, Resort, Facilities, Slots


class loginForm(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class ownerForm(forms.ModelForm):
    class Meta:
        model=Owner
        fields=('name','contact_number','email')


class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('name','contact_number','email','address')

class resortForm(forms.ModelForm):
    class Meta:
        model=Resort
        fields=('name','description','picture','price')

class facilitiesForm(forms.ModelForm):
    class Meta:
        model=Facilities
        fields='__all__'
        exclude=['resort']

class slote_form(forms.ModelForm):
    class Meta:
        model=Slots
        fields=('from_date','to_date')