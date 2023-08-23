import uuid

from django.db import models
from phone_field import PhoneField

# Create your models here.
def generate_unique_id():
    while True:
        u_id = uuid.uuid4().hex[:6].upper()
        if not UserProfile.objects.filter(userID=u_id).exists():
            break
    return u_id

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    about = models.TextField(default='Write something about this product', blank=True, null=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=100, help_text='Enter Full Name')
    designations = models.CharField(max_length=150)
    image = models.ImageField(upload_to='User image')
    userID = models.CharField(max_length=6, default=generate_unique_id, unique=True)
    email = models.EmailField(unique=True)
    number = PhoneField(blank=True, help_text='Contact phone number')
    presentAddress = models.TextField()
    permanentAddress = models.TextField()
    joiningDate = models.DateField()
    NIDNumber = models.IntegerField(unique=True)
    educationQualification = models.CharField(max_length=200)
    eduQuaImg = models.FileField(upload_to='User Edu Qua', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    about = models.TextField(default='About This Employee', blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.designations


class StoreItem(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    totalPrice = models.IntegerField()
    quantity = models.IntegerField()
    amount = models.IntegerField()
    currentBalance= models.IntegerField()
    openingBalance= models.IntegerField()
    closingBalance= models.IntegerField()
    Balance= models.IntegerField()
    refund= models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category + ' ' + self.currentBalance