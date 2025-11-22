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