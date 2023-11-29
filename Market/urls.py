from django.urls import path

from Market import views

app_name="Market"

urlpatterns = [
    # path('',views.home, name='Landingpage'),
    path('home',views.index, name='Home'),
    path('products',views.products,name='Product'),
    path('about',views.about,name='About'),
    path('news',views.news,name='News'),
    path('contact',views.contact,name='Contact'),
    path('add',views.cart,name='add'),
    path('login',views.login,name='Login'),
    path('register',views.register,name='Register'),
    path('insert',views.adduser, name="insertadata"),
    path('insertproduct',views.addproduct,name="insertproduct"),
    path('mydata',views.mydata,name='MyData'),
    path('delete/<id>',views.delete, name="delete"),
    path('edit/<id>',views.edit,name="edit"),
    path('profile',views.profile,name='Profile'),
    path('pay',views.pay,name='pay'),
    path('purchase',views.purchase,name='purchase')
    
]