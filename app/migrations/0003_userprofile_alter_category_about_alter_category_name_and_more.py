# Generated by Django 4.2.4 on 2023-08-17 19:00

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_category_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Full Name', max_length=100)),
                ('designations', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='User image')),
                ('userID', models.CharField(default=uuid.uuid4, max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('number', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('presentAddress', models.TextField()),
                ('permanentAddress', models.TextField()),
                ('joiningDate', models.DateField()),
                ('NIDNumber', models.IntegerField(unique=True)),
                ('educationQualification', models.CharField(max_length=200)),
                ('eduQuaImg', models.ImageField(blank=True, null=True, upload_to='User Edu Qua')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('about', models.TextField(blank=True, default='About This Employee', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='about',
            field=models.TextField(blank=True, default='Write something about this product', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.CreateModel(
            name='StoreItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('totalPrice', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('currentBalance', models.IntegerField()),
                ('openingBalance', models.IntegerField()),
                ('closingBalance', models.IntegerField()),
                ('Balance', models.IntegerField()),
                ('refund', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
    ]