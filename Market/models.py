from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField
# Create your models here.

class Farmer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    image=models.ImageField(upload_to="uploaded/images",default="profile.jpg")
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.firstnname

class User(models.Model):
    fullname = models.CharField(max_length=255)
    phone=models.IntegerField() 
    email=models.EmailField()
    password=models.TextField(max_length=200)
    usertype=models.TextField(max_length=10)
    color = ColorField(default='#FF0000')
    
    def __str__(self):
        return self.fullname

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    image=models.ImageField(upload_to="uploaded/images",default="profile.jpg")
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.firstnname
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    Category = models.CharField(max_length=255,null=True)
    price=models.IntegerField()
    image=models.ImageField(upload_to="uploaded/images",default="profile.jpg")
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

class Staff(models.Model):
    fullname = models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    image=models.ImageField(upload_to="uploaded/images",default="profile.jpg")
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.fullname

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(upload_to="uploaded/images",default="profile.jpg")
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.title
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.product_qty

   

