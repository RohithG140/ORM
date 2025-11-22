# Ex01 Django ORM Web Application
## Date: 

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM

"""
model.py 

from django.db import models
from django.contrib import admin
class amazon(models.Model):
	product_Name=models.CharField(max_length=100)
	serial_Number=models.IntegerField()
	manufacture_date=models.DateField()
	expire_date=models.DateField()
	product_quantity=models.IntegerField()
	price=models.IntegerField()
	delivery_date=models.DateField()


class amazonAdmin(admin.ModelAdmin):
	list_display=["product_Name","serial_Number","manufacture_date","expire_date","product_quantity","price","delivery_date"]

admin.py

from django.contrib import admin
from .models import (amazon,amazonAdmin)
admin.site.register(amazon,amazonAdmin)


"""

## OUTPUT
![alt text](<Screenshot (14).png>)


## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
