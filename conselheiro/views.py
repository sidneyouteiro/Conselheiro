from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.mail import send_mail,EmailMultiAlternatives 
from django.utils.dateparse import parse_duration
import yahoo_fin.stock_info as si
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy

def logon(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        ctx = {}
        if request.method == 'POST':
            username = request.POST.get('usuario')
            password = request.POST.get('senha')
            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('homePage')
            else:
                ctx['msg']='Usuario ou Senha incorretos'
                form = FormsLogin()
                ctx['form']=form
            return render(request,'login.html',ctx)
        else:
            form = FormsLogin()
            ctx['form']=form
            return render(request,'login.html',ctx)

def registro(request):
    if request.user.is_authenticated:
        return redirect('homePage')
    else:
        form = FormRegistro()
        if request.method == 'POST':
            form = FormRegistro(request.POST)
            if form.is_valid():
                form.save()
                return redirect('loginPage')
            else:
                ctx = {'form':form}
                return render(request,'registrese.html',ctx)
        else:
            return render(request,'registrese.html',{'form':form})

class AtualizarEmail(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ['email']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('perfilPage')


@login_required      
def home(request):
    ativos = Tracking.objects.filter(user=request.user)
    live_stock = []
    for ativo in ativos:
        live_stock.append(si.get_live_price(ativo.nome_ativo))
    ativos = zip(ativos,live_stock)
    return render(request,'home.html',{'ativos':ativos})

    
    def save(self, user=None):
        user_profile = super(FormsAddAtivo, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile
@login_required
def perfil(request):
    return render(request,'perfil.html')

@login_required
def addAtivos(request):
    if request.method == 'GET':
        form = FormsAddAtivo()
        return render(request,'addAtivos.html',{'form':form})
    else:
        form = FormsAddAtivo(request.POST)
        print(request.user)
        if form.is_valid():
            nome_ativo = form.cleaned_data.get('nome_ativo')+'.SA'
            periodicidade = parse_duration(form.cleaned_data.get('periodicidade'))
            upper_bound = form.cleaned_data.get('upper_bound')
            lower_bound = form.cleaned_data.get('lower_bound')
            ativo = Tracking(user=request.user,nome_ativo=nome_ativo,periodicidade=periodicidade,upper_bound=upper_bound,lower_bound=lower_bound)
            ativo.save()
            return redirect('homePage')
        else:
            ctx={}
            return render(request,'addAtivos.html',)

class AtualizarTracking(LoginRequiredMixin,generic.UpdateView):
    model = Tracking
    fields = ['nome_ativo','upper_bound','lower_bound','periodicidade']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('homePage')

class DeletarTracking(LoginRequiredMixin,generic.DeleteView):
    model = Tracking
    success_url = reverse_lazy('homePage')