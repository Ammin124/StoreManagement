from django.contrib import admin
from .models import Category, UserProfile, StoreItem

# Register your models here.

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(StoreItem)