from django.shortcuts import render, redirect

from Booking_app.forms import UserForm
from Booking_app.models import User, Facilities, Slots, Resort, Booking, Chat


def customer_dash(request):
    return render(request,'custemer/custemer_base.html')

def customer_profile(request):
    userdata=request.user
    customer_data=User.objects.get(user=userdata)
    return render(request,'custemer/customer_profile.html',{'customer_data':customer_data})

def update_customer_profile(request,id):
    customer_data=User.objects.get(id=id)
    form=UserForm(instance=customer_data)
    if request.method=="POST":
        form1=UserForm(request.POST,instance=customer_data)
        if form1.is_valid():
            form1.save()
            return redirect('customer_profile')
    return render(request,'custemer/customer_profile_update.html',{'form':form})

def view_details(request,id):
    resort=Resort.objects.get(id=id)

    if request.user.is_authenticated:
        return render(request, 'resort_detail.html', {'resort': resort})
    else:
        return redirect('Login')




def view_slot(request,resort_id):
    fac=Facilities.objects.get(resort=resort_id)
    print(fac)
    slot=Slots.objects.filter(fecility=fac)
    print(slot)
    return render(request,'owner/view_slot.html',{'facilities':slot})

def select_slot(request, id):
    user = User.objects.get(user = request.user)
    slot = Slots.objects.get(id = id)
    print(user)
    print(slot)

    if request.method == 'POST':
        booking = Booking()
        booking.user = user
        booking.slot = slot
        booking.save()
        return redirect('booking_success',)

    return render(request, 'custemer/select_slot.html', {
        'user': user,
        'slot': slot
    })

def booking_success(request):
    return render(request,'custemer/booking_success.html')



def bookings_history(request):
    user=User.objects.get(user=request.user)
    history=Booking.objects.filter(user=user)
    return render(request,'custemer/bookings_history.html',{"history":history})

def Chat_with(request,id):
    booking=Booking.objects.get(id=id)
    custemer=User.objects.get(user=request.user)
    data=booking.slot.fecility.resort
    if request.method == "POST":
        chat=Chat()
        chat.customer=custemer
        chat.resort=data
        chat.message = request.POST.get('message')
        chat.save()
        return redirect('bookings_history')
    return render(request,'custemer/chat.html', {"booking":booking,"custemer":custemer})