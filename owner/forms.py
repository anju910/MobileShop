from django import forms
from django.forms import ModelForm
from .models import Mobile,Brand
from customer.models import Orders

class BrandCreationForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={"class":"form-control"}),
        }


class BrandSearchForm(forms.Form):
    brand_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={"class":"form-control"}))


class BrandUpdateForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={"class":"form-control"}),
        }



class MobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={"class":"form-control"}),
            "brand":forms.Select(attrs={"class":"form-select"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "memory": forms.TextInput(attrs={"class": "form-control"}),
            "os": forms.TextInput(attrs={"class": "form-control"}),
            "specs": forms.TextInput(attrs={"class": "form-control"}),
            "images": forms.FileInput(attrs={"class": "form-control"}),
        }

class OrderUpdateForm(ModelForm):
    class Meta:
        model=Orders
        fields=[
            "status","product","qty"
        ]
        widgets={
            "status":forms.Select(attrs={"class":"form-select"}),
            "product": forms.TextInput(attrs={"class": "form-control","readonly":True}),
            "qty": forms.NumberInput(attrs={"class": "form-control", "readonly": True}),

        }

