from django.shortcuts import render

# Create your views here.
def Rest_index(request):
    return render(request,'index.html')

def dash_board(request):
    return render(request,'dashboard.html')

def loging(request):
    return render(request,'reg_log.html')