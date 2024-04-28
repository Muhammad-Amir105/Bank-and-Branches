from django import forms
from django.contrib.auth.forms import UserCreationForm  , UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100 , widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username' , 'password1' , 'password2' , 'email' , 'first_name' , 'last_name']
        

class customuserchange(UserChangeForm):
    password1 =forms.CharField(widget=forms.PasswordInput)
    password2 =forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username' , 'password1' , 'password2' , 'email' , 'first_name' , 'last_name']


        def save(self , commit=True):
            user=super().save(commit=False)
            password1=self.cleaned_data.get('password1')
            password2=self.cleaned_data.get('password2')

            if password1 and password2:
                user.set_password(password1)
                user.save()
                user=authenticate(username=user.username , password=password1)
                login(self.request , user)
            elif not password1 and not password2:
                pass
            else:
                user.ser_password(self.cleaned_data.get('password' , user.password))

            if commit:
                user.save()
            return user



