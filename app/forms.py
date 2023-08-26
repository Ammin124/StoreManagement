from django import forms
from .models import Category, Vendor, UserProfile, StoreItem

class CategoryForms(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category Name'}))
    about = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Say something about your category', 'style': 'height:20px;'}))
    class Meta:
        model = Category
        fields = ('name', 'about', 'image')

        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'image': '',
        }
