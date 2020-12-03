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

class FormsAddAtivo(forms.Form):
    nome_ativo = forms.CharField(max_length=10,widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
         'placeholder':'Ticker do Ativo',
         'id':'nome_ativo',
    }))

    periodo = (
        (None,'Periodicidade do Ativo'),
        ('00:15:00','00:15:00'),
        ('00:30:00','00:30:00'),
        ('00:45:00','00:45:00'))
    periodicidade = forms.ChoiceField(choices=periodo,widget=forms.Select(attrs={
        'class':'form-control mb-3',
         'placeholder':'Ticker do Ativo',
         'id':'periodicidade',
    }))

    upper_bound = forms.DecimalField(widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'Upper Bound do Ativo',
        'id':'upper_bound',
    }))

    lower_bound = forms.DecimalField(widget=forms.TextInput(attrs={
        'class':'form-control mb-3',
        'placeholder':'Lower Bound do Ativo',
        'id':'lower_bound',
    }))

    class Meta:
        model = Tracking
        fields = ('nome_ativo','periodicidade','upper_bound','lower_bound')