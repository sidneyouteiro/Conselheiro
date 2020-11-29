from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from .forms import *
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 

def logon(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        if request.method == 'POST':
            username = request.POST.get('usuario')
            password = request.POST.get('senha')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                print('b')
                login(request,user)
                return redirect('homePage')
            else:
                print('c')
                messages.info(request,'Login ou Senha incorretos')

            ctx = {}
            print('d')
            return render(request,'login.html')
        else:
            form = FormsLogin()
            return render(request,'login.html',{'form':form})

def registro(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        form = FormRegistro()
        if request.method == 'POST':
            form = FormRegistro(request.POST)
            if form.is_valid():
                form.periodo = None
                form.save()
                return redirect('loginPage')
            else:
                ctx = {'form':form}
                return render(request,'registrese.html',ctx)
        else:
            return render(request,'registrese.html',{'form':form})

@login_required      
def home(request):
    return render(request,'pos_login_base.html')

def perfil(request):
    return render(request,'perfil.html')