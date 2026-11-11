from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Booking_app.forms import UserForm, ownerForm
from Booking_app.models import User, Owner, Resort

@login_required(login_url='Login')
def admin_dash(request):
    return render(request,'admin/admin_base.html')
#
# def view_customer(request):
#     return render(request,'admin/view_customer.html')



#customer List viewing by admin
@login_required(login_url='Login')
def customer_list(request):
    data=User.objects.all()
    return render(request,'admin/view_customer.html',{'data':data})

@login_required(login_url='Login')
def delete_customer(request,id):
    data=User.objects.get(id=id)
    data.delete()
    return redirect('view_customer')

@login_required(login_url='Login')
def update_customer(request,id):
    data=User.objects.get(id=id)
    form=UserForm(instance=data)
    if request.method=='POST':
        form1=UserForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('view_customer')
    return render(request,'admin/update_cstomer.html',{'form':form})



#owner List viewing by admin
@login_required(login_url='Login')
def owner_List (request):
    data=Owner.objects.all()
    return render(request,'admin/view_owner.html',{'data':data})

@login_required(login_url='Login')
def delete_owner(request,id):
    data=Owner.objects.get(id=id)
    data.delete()
    return redirect('view_owner')

@login_required(login_url='Login')
def update_owner(request,id):
    data=Owner.objects.get(id=id)
    form=ownerForm(instance=data)
    if request.method=='POST':
        form1=ownerForm(request.POST,instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('view_owner')
    return render(request,'admin/update_owner.html',{'form':form})


@login_required(login_url='Login')
def View_all_resort(request):
    resort=Resort.objects.all()
    return render(request,'admin/view_all_resort.html',{'resorts':resort})

