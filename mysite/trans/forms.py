from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Video
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class VideoForm(ModelForm):
    class Meta:
        model=Video
        fields="__all__"
