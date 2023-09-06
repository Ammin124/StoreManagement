from django.contrib import admin
from .models import Category, Vendor, UserProfile
# Register your models here.

admin.site.register(Category)
admin.site.register(Vendor)
admin.site.register(UserProfile)
