from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from .models import Category, Vendor, UserProfile
from .forms import CategoryForms, VendorForms, ProfileForms

# Create your views here.
# ---------------------------------------- Home Section ------------------------------------
def home(request):
    return render(request,'home/index.html')
# ---------------------------------------- End  Home Section ------------------------------------
# ---------------------------------------- User Login Section ------------------------------------
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
# ---------------------------------------- End User Login Section ------------------------------------
# ----------------------------------------  User Logout Section ------------------------------------
def logoutUser(request):
    logout(request)
    messages.success(request, "logout your account ?")
    return redirect('login')
# ---------------------------------------- User Logout Section ------------------------------------
# ---------------------------------------- Category Section ------------------------------------
def category(request):
    if request.method == 'POST':
        catForms = CategoryForms(request.POST, request.FILES)
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
# ---------------------------------------- End Category Section ------------------------------------
# ---------------------------------------- Category Update Section ------------------------------------
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
# ---------------------------------------- End Category Update Section ------------------------------------
# ---------------------------------------- Vendor Section ------------------------------------
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
    else:
        venForms = VendorForms()
    vendorData = Vendor.objects.all()

    context = {
        'venForms': venForms,
        'vendorData': vendorData,
    }
    return render(request, 'home/vendor.html', context)
# ---------------------------------------- End Vendor Section ------------------------------------
# ---------------------------------------- Vendor Update Section ------------------------------------
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
# ---------------------------------------- End Vendor Update Section ------------------------------------
# ---------------------------------------- Vendor Details Section ------------------------------------
def vendorDetails(request, id):
    ven = Vendor.objects.get(pk=id)
    context = {
        'ven': ven,
    }
    return render(request, 'home/vendorDetails.html', context)
# ---------------------------------------- End Vendor Details Section ------------------------------------
# ---------------------------------------- User Profile Section ------------------------------------
def profile(request):
    if request.method == 'POST':
        proForms = ProfileForms(request.POST, request.FILES)
        if proForms.is_valid():
            name= proForms.cleaned_data['name']
            des = proForms.cleaned_data['designations']
            image = proForms.cleaned_data['image']
            email = proForms.cleaned_data['email']
            phone = proForms.cleaned_data['phone']
            preAdd = proForms.cleaned_data['presentAddress']
            perAdd = proForms.cleaned_data['permanentAddress']
            join = proForms.cleaned_data['joiningDate']
            NIDNum = proForms.cleaned_data['NIDNumber']
            edu = proForms.cleaned_data['educationQualification']
            about = proForms.cleaned_data['about']
            eduImg = proForms.cleaned_data['eduQuaImg']
            proData = UserProfile(name=name, designations=des, image=image, email=email, phone=phone, presentAddress=preAdd,
                                   permanentAddress=perAdd, joiningDate=join, NIDNumber=NIDNum, educationQualification=edu,
                                  about=about, eduQuaImg=eduImg)
            proData.save()
            proForms = ProfileForms()
    else:
        proForms = ProfileForms()
    profileData = UserProfile.objects.all()
    context = {
        'proForms': proForms,
        'profileData': profileData,
    }
    return render(request, 'home/userProfile.html', context)

# ---------------------------------------- Eng User Profile Section ------------------------------------