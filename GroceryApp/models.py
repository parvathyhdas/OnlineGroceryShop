from django.db import models

# Create your models here.
class CategoryDB(models.Model):

    CategoryName = models.CharField(max_length=50,null=True,blank=True)
    Description = models.CharField(max_length=50,null=True,blank=True)
    CategoryImage = models.ImageField(upload_to="Images",null=True,blank=True)

class ProductDB(models.Model):
    ProductName = models.CharField(max_length=50, null=True, blank=True)
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Price = models.CharField(max_length=50, null=True, blank=True)
    ProductImage = models.ImageField(upload_to="ProductImages", null=True, blank=True)

