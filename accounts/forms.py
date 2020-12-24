from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from visitors.models import Customer    

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']



class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer 
        exclude = ['user'] 


