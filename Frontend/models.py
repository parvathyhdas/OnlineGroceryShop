from django.db import models

# Create your models here.
class ContactDB(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    Email = models.CharField(max_length=50,null=True,blank=True)
    Message = models.CharField(max_length=50,null=True,blank=True)

class SignUPDB(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Mobile = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    UserName = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)

class CartDB(models.Model):
    UserName = models.CharField(max_length=50, null=True, blank=True)
    ProductName = models.CharField(max_length=50, null=True, blank=True)
    Quntity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)

class OrderDB(models.Model):
    boolChoice = (
        ("C", "CreditCard"), ("D", "DebitCard"), ("P", "Paypal")
    )
    FirstName = models.CharField(max_length=50,null=True,blank=True)
    LastName = models.CharField(max_length=50,null=True,blank=True)
    UserName = models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(null=True,blank=True)
    Address = models.CharField(max_length=500,null=True,blank=True)
    Country = models.CharField(max_length=50,null=True,blank=True)
    State = models.CharField(max_length=50,null=True,blank=True)
    Pin = models.IntegerField(null=True,blank=True)
    Payment = models.CharField(max_length=1, choices=boolChoice)
    NameOnCard = models.CharField(max_length=50, null=True, blank=True)
    CardNumber = models.IntegerField(null=True, blank=True)
    Expiration = models.CharField(max_length=50,null=True, blank=True)
    CVV = models.CharField(max_length=50,null=True, blank=True)


