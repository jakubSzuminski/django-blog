from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

#Create a UserRegisterForm based on UserCreationForm
#but add additional "email" field
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
