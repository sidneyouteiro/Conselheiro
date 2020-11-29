from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import *
from datetime import datetime

class FormRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class FormTrocaPeriodo(UserChangeForm):
    class Meta:
        model = User
        fields = ('periodo',)

class FormsLogin(forms.Form):
     usuario = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
         'class':'form-control mb-3',
         'placeholder':'Login',
         'id':'Login',
     }))
     senha = forms.CharField(widget=forms.PasswordInput(attrs={
         'class':'form-control',
         'placeholder':'Senha',
         'id':'Senha',
     }))


# class FormsRegistro(forms.Form):
#     nome = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
#         'class':'form-control mb-3',
#         'placeholder':'Nome',
#         'id':'Nome',
#     }))
    
#     email = forms.EmailField(max_length=100,widget=forms.EmailInput(attrs={
#         'class':'form-control mb-3',
#         'placeholder':'Email',
#         'id':'Email',
#     }))

#     senha1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
#         'class':'form-control mb-3',
#         'placeholder':'Senha',
#         'id':'Senha1',
#     }))

#     senha2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
#         'class':'form-control',
#         'placeholder':'Digite novamente a senha',
#         'id':'Senha2',
#     }))

# class bdRegistro(UserCreationForm):
#     class Meta:
#         model = Usuario
#         fields = ('nome','senha','email')