from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from visitors.models import Customer    
# from .models import CustomUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']



class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer 
        exclude = ['user'] 





# this methode is the for the signup version 
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields+ ('age',)
# # here are are using the usercreatioform basic fiellds plus we add the customForm 

# class CustomerChangeForm(UserChangeForm):
#     model = CustomUser
#     fields = UserChangeForm.Meta.fields