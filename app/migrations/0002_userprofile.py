# Generated by Django 4.2.4 on 2023-09-02 13:03

import app.models
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designations', models.CharField(max_length=150)),
                ('image', models.ImageField(help_text='jpg or  png image', upload_to='User image')),
                ('userID', models.CharField(default=app.models.generate_unique_id, max_length=6, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('presentAddress', models.TextField()),
                ('permanentAddress', models.TextField()),
                ('joiningDate', models.DateField()),
                ('NIDNumber', models.IntegerField(unique=True)),
                ('educationQualification', models.CharField(max_length=200)),
                ('eduQuaImg', models.FileField(blank=True, help_text='only pdf file', null=True, upload_to='User Edu Qua')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
