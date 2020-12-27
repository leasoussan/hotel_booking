from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from visitors.models import Customer
from accounts.forms import MyUserCreationForm, CustomerCreateForm
from django.contrib.auth.forms import UserCreationForm

class Register(View):
    def get(self, request):
        context = {
         "form": MyUserCreationForm(),   
         "form2": CustomerCreateForm()
        }
        return render(request, 'registration/register.html', context)

    def post(self, request):
        form = MyUserCreationForm(request.POST)
        form2 = CustomerCreateForm(request.POST)
        if form.is_valid() and form2.is_valid:
            user = form.save()
            customer = form2.save(commit = False)
            customer.user = user 
            customer.save()
    
            user = authenticate(username= form.cleaned_data['username'], password =form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'registration/register.html', {"form":form, "form2":form2})      


# when I do the user = authenticate.... it's because I wouldlike to get the details to automaticaly log the user 
# to make sure the username and passowrd are correcte



# another way to do the registration form: 

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


