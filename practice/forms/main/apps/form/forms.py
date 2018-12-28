from django import forms
from .models import 
class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=45)
    last_name = forms.CharField(max_length=45)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    pw_confirm = forms.CharField(max_length=100, widget=forms.PasswordInput)
