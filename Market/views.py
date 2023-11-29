from django.shortcuts import render,redirect,get_object_or_404
from .models import Products,User,Staff,Cart,Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here
 
    
def index(request):
   data_from_db = Products.objects.all() 
   return render(request ,'index.html', {'data': data_from_db})

def products(request):
    data_from_db = Products.objects.all()
    return render(request,'products.html', {'data':data_from_db})

def about(request):
    data_from_db = Staff.objects.all() 
    return render(request,'about.html', {'data': data_from_db})

def news(request):
    data_from_db = Blog.objects.all()
    return render(request,'news.html',{'data':data_from_db})

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email, password=password).first()
        if user:
            # If user exists and passwords match, consider user as authenticated
            # You may want to use more secure methods for password handling (like hashing)
            request.session['user_id'] = user.id  # Store user ID in session
            return redirect("/home")  
        else:
            # Handle invalid login
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')

def register(request):
    return render(request,'register.html')

def adduser(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password=request.POST.get('password')
        usertype=request.POST.get('usertype')
        
        query= User(fullname=fullname,email=email,phone=phone,password=password,usertype=usertype)
        query.save()

                
      
    return redirect("/login")

def mydata(request):
    data_from_db = Products.objects.all() 
    return render(request,'crud.html',{'data': data_from_db})

def addproduct(request):
       if request.method =="POST":
          name = request.POST.get('name')
          Category = request.POST.get('Category')
          price = request.POST.get('price')
        
          if len(request.FILES) !=0:
                image=request.FILES['image']

                query= Products(name=name,Category=Category,price=price,image=image)
                query.save()
                
                return redirect("/mydata")
        
       return redirect("/mydata")

def delete(request,id):
    product=Products.objects.get(id=id)
    product.delete()
    
    return redirect("/mydata")

def edit(request,id):

    if request.method =="POST":
        name=request.POST.get('name')
        Category=request.POST.get('Category')
        price=request.POST.get('price')
        image=request.POST.get('image')
        
        product=Products.objects.get(id=id)

        product.name = name 
        product.Category =Category
        product.price=price
        product.image=image

        product.save()
        
        return redirect("/mydata")

        
    product=Products.objects.get(id=id)
    return render(request,'edit.html',{'product':product})


def profile(request):
    return render(request,'profile.html')

def add(request):
    data = Products.objects.all() 
    return render(request,'cart.html', {'data': data})
    

def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})



def pay(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Ragama",
            "TransactionDesc": "Pay"
        
        }

    response = requests.post(api_url, json=request, headers=headers)
    return render(request, 'products.html')

    


def purchase(request):
    return render(request, 'pay.html')
 

   