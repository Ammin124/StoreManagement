from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Category, Vendor, UserProfile, StoreItem
from .forms import CategoryForms

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

def category(request):
    if request.method == 'POST':
        catForms = CategoryForms(request.POST)
        if catForms.is_valid():
            name = catForms.cleaned_data['name']
            about = catForms.cleaned_data['about']
            image = catForms.cleaned_data['image']
            catData = Category(name=name, about=about, image=image)
            catData.save()
        catForms = CategoryForms()
    else:
        catForms = CategoryForms()
    categoryData = Category.objects.all()

    context = {
        'catForms': catForms,
        'categoryData': categoryData,
    }
    return render(request,'home/category.html', context)