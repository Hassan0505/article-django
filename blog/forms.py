from django import forms
from .models import Article

class UserRegisterationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



