from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    description = models.CharField(max_length=500)
    product_available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)