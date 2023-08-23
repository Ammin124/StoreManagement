from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'home/index.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have login")
            return redirect('home')

        else:
            messages.success(request,"try Again")
            return redirect('login')
    else:
        return render(request,'auth/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request, "logout your account ?")
    return redirect('login')