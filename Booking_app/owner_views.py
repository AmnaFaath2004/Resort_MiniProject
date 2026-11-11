from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Booking_app.forms import UserForm, ownerForm, resortForm, facilitiesForm, slote_form
from Booking_app.models import User, Owner, Resort, Facilities, Slots, Booking, Chat

@login_required(login_url='Login')
def owner_dash(request):
    return render(request,'owner/owner_base.html')


@login_required(login_url='Login')
def profile(request):
    userdata=request.user
    #print("last login :",userdata,userdata.id)
    owner_data=Owner.objects.get(user=userdata)
                                                 #(user=userdata)=this user is from owner model

    #print("id : ", owner_data.id)
    #print("name :", owner_data.name)
    #print("Phone :", owner_data.contact_number)
    #print("Email :", owner_data.email)
    return render(request,'owner/owner_profile.html',{'owner_profile_data':owner_data})


@login_required(login_url='Login')
def Update_profile(request,id):
    data=Owner.objects.get(id=id)
    form=ownerForm(instance=data)
    if request.method=='POST':
        form1=ownerForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('profile')
    return render(request,'owner/owner_profile_update.html',{'form':form})

@login_required(login_url='Login')
def resort(request):
    form=resortForm()
    data=Owner.objects.get(user=request.user)
    if request.method=='POST':
        form=resortForm(request.POST,request.FILES)
        if form.is_valid():
            resort=form.save(commit=False)
            resort.owner=data
            resort.save()
            return redirect('facilities',resort_id=resort.id)
    return render(request,'owner/resort.html', {'form':form})

# def view_resort(request,resort_id):
#     resort=Resort.objects.get(id=resort_id)
#     facilities=Facilities.objects.filter(resort=resort)
#     return render(request,'owner/view_resort.html',{'resort':resort,'facilities':facilities})

@login_required(login_url='Login')
def view_resort(request):
    owner = Owner.objects.get(user=request.user)
    resorts = Resort.objects.filter(owner=owner)


    return render(request, 'owner/view_resort.html', {
        'resort': resorts

    })

@login_required(login_url='Login')
def edit_resort(request,id):
    data=Resort.objects.get(id=id)
    form=resortForm(instance=data)
    if request.method=='POST':
        form1=resortForm(request.POST,request.FILES,instance=data)
        if form1.is_valid():
            resort=form1.save()
            return redirect('edit_facilities',resort_id=resort.id)
    return render(request,'owner/edit_resort.html',{'form':form})

@login_required(login_url='Login')
def delete_resort(request,resort_id):
    owner=Owner.objects.get(user=request.user)
    resort_data=Resort.objects.get(id=resort_id,owner=owner)
    resort_data.delete()
    return redirect('view_resort')


@login_required(login_url='Login')
def facilities(request,resort_id):
    data=Resort.objects.get(id=resort_id)
    form=facilitiesForm()

    if request.method=='POST':
        form=facilitiesForm(request.POST)

        if form.is_valid():
            facilities= form.save(commit=False)
            facilities.resort=data
            facilities.save()
            return redirect('owner_dash')
    return render(request,'owner/facilities.html',{'form':form})


@login_required(login_url='Login')
def edit_facilities(request,resort_id):
    resort=Resort.objects.get(id=resort_id)
    data=Facilities.objects.get(resort=resort)

    form=facilitiesForm(instance=data)
    if request.method=='POST':
        form1=facilitiesForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('view_resort')
    return render(request,'owner/edit_facilities.html',{'form':form})


@login_required(login_url='Login')
def slot(request,fec_id):
    form=slote_form()
    data=Facilities.objects.get(resort=fec_id)
    print(data)
    if request.method=='POST':
        form1=slote_form(request.POST)
        if form1.is_valid():
            slote=form1.save(commit=False)
            slote.fecility=data
            slote.save()
            return redirect('view_resort')
    return render(request,'owner/slote.html',{'form':form})

@login_required(login_url='Login')
def view_slot_Owner(request):
    owner=Owner.objects.get(user=request.user)
    slot=Slots.objects.filter(fecility__resort__owner=owner)
    return render(request,'owner/view_slot_Owner.html',{'slots':slot})

@login_required(login_url='Login')
def delete_slot(request,id):
    owner=Owner.objects.get(user=request.user)
    slot=Slots.objects.get(id=id,fecility__resort__owner=owner)
    slot.delete()
    return redirect('view_slot_Owner')


@login_required(login_url='Login')
def viewing_bookings(request):
    owner = Owner.objects.get(user=request.user)
    history = Booking.objects.filter(slot__fecility__resort__owner=owner)
    return render(request,'owner/viewing_bookings.html',{'history':history})


@login_required(login_url='Login')
def for_approval(request,id):
    bookings=Booking.objects.get(id=id)
    bookings.status = 1
    bookings.save()

    slot=bookings.slot
    slot.slot_status= True
    slot.save()

    return redirect('viewing_bookings')

@login_required(login_url='Login')
def for_reject(request,id):
    bookings=Booking.objects.get(id=id)
    bookings.status = 2
    bookings.save()
    return redirect('viewing_bookings')

@login_required(login_url='Login')
def view_messages(request):
    owner = Owner.objects.get(user=request.user)
    messages = Chat.objects.filter(resort__owner=owner)
    return render(request,'owner/view_messages.html',{'messages':messages})

@login_required(login_url='Login')
def replying(request,id):
    chat=Chat.objects.get(id=id)
    if request.method=='POST':
        chat.reply = request.POST.get('reply')
        chat.save()
        return redirect('view_messages')
    return render(request, 'owner/replying.html')






