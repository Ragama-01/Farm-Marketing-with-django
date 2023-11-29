
from django import forms
from .models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'lastname','password','email'] 
