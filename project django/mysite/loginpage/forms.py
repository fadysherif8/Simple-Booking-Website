from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms import ModelForm
from .models import Signin

class Signinform(forms.Form):
    Email=forms.EmailField(label='Email',max_length=None)
    passw=forms.CharField(widget=forms.PasswordInput,label='Password',max_length=20)
    #class Meta:
     #   model=Signin
      #  fields='__all__'