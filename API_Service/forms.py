from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import logging

logger = logging.getLogger(__name__)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not username or not password:
            raise forms.ValidationError("Username and password are required.")

        user = authenticate(username=username, password=password)
        if user is None:
            logger.error("Login failed for user: %s", username)
            raise forms.ValidationError("Invalid username or password.")
        else:
            logger.info("Login successful for user: %s", username)
        return cleaned_data