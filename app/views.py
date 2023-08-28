from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse

from .models import Category, Vendor, UserProfile, StoreItem
from .forms import CategoryForms, VendorForms

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

def updateCategory(request, id):
    if request.method == 'POST':
        upCat = Category.objects.get(pk=id)
        catForms = CategoryForms(request.POST, instance=upCat)
        if catForms.is_valid():
            catForms.save()
    else:
        upCat = Category.objects.get(pk=id)
        catForms = CategoryForms(instance=upCat)
    context = {
        'catForms': catForms,
    }
    return render(request, 'home/updateCategory.html', context)

def vendor(request):
    if request.method == 'POST':
        venForms = VendorForms(request.POST)
        if venForms.is_valid():
            name = venForms.cleaned_data['name']
            productType = venForms.cleaned_data['productType']
            email = venForms.cleaned_data['email']
            phone = venForms.cleaned_data['phone']
            address = venForms.cleaned_data['address']
            bank = venForms.cleaned_data['bank']
            contact = venForms.cleaned_data['contact']
            vanData = Vendor(name=name, productType=productType, email=email, phone=phone,  address=address,
                             bank=bank , contact=contact)
            vanData.save()
        venForms = VendorForms()
    else:
        venForms = VendorForms()
    vendorData = Vendor.objects.all()

    context = {
        'venForms': venForms,
        'vendorData': vendorData,
    }
    return render(request, 'home/vendor.html', context)

def updateVendor(request, id):
    if request.method == 'POST':
        upVat = Vendor.objects.get(pk=id)
        vanForms = VendorForms(request.POST, instance=upVat)
        if vanForms.is_valid():
            vanForms.save()
            return redirect(reverse('vendor'))
    else:
        upVat = Vendor.objects.get(pk=id)
        vanForms = VendorForms(instance=upVat)
    context = {
        'vanForms': vanForms,
    }
    return render(request, 'home/updateVendor.html', context)

def vendorDetails(request, id):
    ven = Vendor.objects.get(pk=id)
    context = {
        'ven': ven,
    }
    return render(request, 'home/vendorDetails.html', context)