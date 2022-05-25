from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput


from place.models import Place
from home.models import Profile
from django.contrib.auth import logout, authenticate, login

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name' )
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'})
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'address', 'image')
        widgets = {
            'phone' : TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}),
            'address': TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'})
        }

class Yer_GirForm(forms.ModelForm):
    class Meta:

        model = Place
        fields = ('title', 'keywords', 'description', 'image', 'detail', 'category', 'slug')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'title'}),
            'keywords': TextInput(attrs={'class': 'form-control', 'placeholder': 'keywords'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'description'}),
            'image': FileInput(attrs={'class': 'form-control', 'placeholder': 'image'}),
            'detail': TextInput(attrs={'class': 'form-control', 'placeholder': 'detail'}),
            'category': TextInput(attrs={'class': 'form-control', 'placeholder': 'category'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'})
        }