from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sousadmins


class LoginForm(forms.ModelForm):
    username = forms.CharField(label='username')
    password = forms.CharField(
        label='password', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')




class SousadminsForm(forms.ModelForm):
    class Meta:
        model = Sousadmins
        fields = '__all__'
        widgets = {
            'username'  :   forms.Select(attrs={'class':'form-control'}),
            'nom'  :   forms.TextInput(attrs={'class':'form-control'}),
            'prenom'  :   forms.TextInput(attrs={'class':'form-control'}),
            'email'  :   forms.EmailInput(attrs={'class':'form-control'}),
        }

