from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from customer.models import Orders

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),

        }

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={"class":"form-control"}))


class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["address","qty"]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-control"}),
            "qty":forms.NumberInput(attrs={"class":"form-control"})
        }