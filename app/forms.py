from django import forms
from .models import Category, Vendor, UserProfile
from phonenumber_field.formfields import PhoneNumberField

# ---------------------------------------- Category Forms Section ------------------------------------
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
# ---------------------------------------- Eng Category Forms Section ------------------------------------
# ---------------------------------------- Vendor Forms Section ------------------------------------
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
            'name': '', 'productType': '', 'email': '', 'address': '', 'bank': '', 'contact': '',
        }
# ---------------------------------------- Eng Vendor Forms Section ------------------------------------
# ---------------------------------------- Profile Forms Section ------------------------------------
class ProfileForms(forms.ModelForm):
    phone = PhoneNumberField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number: '}), required=False)
    class Meta:
        model = UserProfile
        fields = ('image', 'name', 'designations',  'email', 'phone', 'presentAddress', 'permanentAddress',
                  'joiningDate', 'NIDNumber', 'educationQualification', 'eduQuaImg', 'about')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name: '}),
            'designations': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Designation'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email: '}),
            'presentAddress': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Present Address: '}),
            'permanentAddress': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Permanent Address: '}),
            'joiningDate': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Joining Date (Year-month-day)'}),
            'NIDNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NID Number: '}),
            'educationQualification': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Education Qualification'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About this employee'}),
            'eduQuaImg': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': '', 'designations': '', 'image': '', 'email': '', 'presentAddress': '', 'permanentAddress': '',
            'joiningDate': '', 'educationQualification': '', 'eduQuaImg': '','NIDNumber':'', 'about': '',
        }
# ---------------------------------------- Eng Profile Forms Section ------------------------------------
