from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name='login'),
    path('home/', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('category/<int:id>', views.updateCategory, name='updateCategory'),
    path('logout/', views.logoutUser, name='logout'),

]
