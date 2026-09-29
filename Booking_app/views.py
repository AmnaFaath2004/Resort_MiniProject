from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from Booking_app.forms import loginForm, ownerForm, UserForm
from Booking_app.models import Facilities, Resort


# Create your views here.
def Rest_index(request):
    return render(request,'index.html')

def dash_board(request):
    return render(request,'dashboard.html')

def Login(request):
    if request.method =="POST":
        username =request.POST.get('uname')
        password =request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                print('admin')
                return redirect('admin_dash')
            elif user.is_owner:
                return redirect('owner_dash')
            elif user.is_user:
                return redirect('customer_dash')
    else:
        print("Invalid Credentials")
    return render(request,'reg_log.html')
#
# def login_form(request):
#     data=loginForm()
#     return render(request,"login_form.html",{'data':data})

def owner_Registration(request):
    data = loginForm()
    owner=ownerForm()
    if request.method =='POST':
        #recieve data from frountend
        data = loginForm(request.POST)
        owner = ownerForm(request.POST)

        if owner.is_valid() and data.is_valid():
            #to sava data to login database
            owr=data.save(commit=False)
            owr.is_owner = True
            owr.save() # a model will create with a  "id"   and loging table of owner is created .(username and passwrd).

            #to save data to owner database
            x=owner.save(commit=False)
            x.user = owr  #that "id"
            x.save()

            return redirect('Login')
    return render(request,'owner_Form.html',{'owner':owner,'data':data})

def User_Registration(request):
    data = loginForm()
    user=UserForm()
    if request.method =='POST':
        data = loginForm(request.POST)
        user = UserForm(request.POST)
        if user.is_valid() and data.is_valid():
            usr=data.save(commit=False)
            usr.is_user   =True
            usr.save()

            y=user.save(commit=False)
            y.user=usr
            y.save()
            return redirect('Login')

    return render(request,'user_Form.html',{'user':user,'data':data})

def listing_resorts(request):
    resorts=Resort.objects.all()

    return render(request, 'index.html',{'resorts':resorts})



def logout_view(request):
    logout(request)
    return redirect('Login')


