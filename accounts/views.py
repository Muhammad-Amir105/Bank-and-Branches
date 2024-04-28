from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from .forms import LoginForm, RegisterForm , customuserchange
from .models import User
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

def User_login(request):
    form = LoginForm()  # Instantiate LoginForm object
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Pass POST data to LoginForm
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # return render(request , 'Banks:Bank/showbank.html')
                return redirect('Userprofile')
            else:
                return render(request, 'accounts/user_login.html', {'form': form})
    return render(request, 'accounts/user_login.html', {'form': form})  # Render the form for GET requests

def user_register(request):
    form = RegisterForm()  # Instantiate RegisterForm object
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Pass POST data to RegisterForm
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = RegisterForm()  # Instantiate RegisterForm object for GET requests
    return render(request, 'accounts/user_register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')

# def costumchanges(request):
#     form=customuserchange()



class Userprofile(LoginRequiredMixin , DetailView):
    model=User
    template_name='accounts/show_profile.html'
    context_object_name='user'

    def get_object(self ):
        return User.objects.filter(username=self.request.user)
