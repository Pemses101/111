# account/forms.py
from django import forms

class LoginForms(forms.Form):
    # Define your form fields here
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
