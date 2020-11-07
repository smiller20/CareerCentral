from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
    username=forms.CharField(max_length=10)
    email=forms.CharField(max_length=20)
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)

    class Meta:
        model=User
        fields=("username"  , "first_name", "last_name" ,  "email" )
