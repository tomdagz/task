from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

        widgets = {
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Tu email'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Tu contrasena'}),
        }

class LoginForm(forms.Form):
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu email'}))
    password = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Tu contrasena'}))
