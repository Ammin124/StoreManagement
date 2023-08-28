from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('home/', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('category/<int:id>', views.updateCategory, name='updateCategory'),
    path('vendor/', views.vendor, name='vendor'),
    path('vendor/<int:id>', views.updateVendor, name='updateVendor'),
    path('vendor/details/<int:id>', views.vendorDetails, name='vendorDetails'),

    path('logout/', views.logoutUser, name='logout'),

]
