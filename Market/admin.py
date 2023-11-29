from django.contrib import admin

from .models import Farmer,Customer,Products,Staff,Blog,User,Cart
# Register your models here.

admin.site.register(Farmer)

admin.site.register(Customer)

admin.site.register(Products)

admin.site.register(Staff)

admin.site.register(Blog)

admin.site.register(User)

admin.site.register(Cart)

admin.site.site_header='PRODUCTS ADMIN PAGE'