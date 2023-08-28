from django import forms
from .models import Category, Vendor, UserProfile, StoreItem
from phonenumber_field.formfields import PhoneNumberField

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

class VendorForms(forms.ModelForm):
    phone = PhoneNumberField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Phone Number'}), required=False)
    class Meta:
        model = Vendor
        fields = ('name', 'productType', 'email', 'phone', 'address', 'bank', 'contact')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Name'}),
            'productType': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Product Type'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Contact Email'}),
            #'phone': forms.PhoneNumberField(attrs={'class': 'form-control', 'placeholder': 'Vendor Phone Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Vendor Address'}),
            'bank': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Vendor Bank Name, Bank Routing Number , Bank Branch Number'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vendor Contact Person'}),
        }
        labels = {
            'name': '',
            'productType': '',
            'email': '',
            'address': '',
            'bank': '',
            'contact': '',
        }