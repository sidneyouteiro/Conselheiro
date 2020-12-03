from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django.core.mail import send_mail
from django.db.models import Q
from django.conf import settings

from conselheiro.models import *
import yahoo_fin.stock_info as si
from django.utils.dateparse import parse_duration



scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)
# This is the function you want to schedule - add as many as you want and then register them in the start() function below


def check15min():
    global i 
    i = 0
    query = Tracking.objects.values('nome_ativo').distinct()
    for nome in query:
        ativo = Ativo(nome_ativo=nome['nome_ativo'],valor=si.get_live_price(nome['nome_ativo']))
        ativo.save()
        trackings2 = list()
        trackings3 = list()
        trackings1 = Tracking.objects.all().filter(nome_ativo=ativo.nome_ativo,periodicidade=parse_duration('00:15:00'))
        if i % 2 == 0:
            trackings2 = Tracking.objects.all().filter(nome_ativo=ativo.nome_ativo,periodicidade=parse_duration('00:30:00'))
        if i % 3 == 0:
            trackings3 = Tracking.objects.all().filter(nome_ativo=ativo.nome_ativo,periodicidade=parse_duration('00:45:00'))
        
        trackings = trackings1 + trackings2 + trackings3
        for tracking in trackings:
            if tracking.upper_bound < ativo.valor:
                upper_bound_trigger(tracking.user, ativo.nome_ativo)
            elif tracking.lower_bound > ativo.valor:
                lower_bound_trigger(tracking.user,ativo.nome_ativo)
        i = i +1

def upper_bound_trigger(user_id,nome_ativo):
    user = User.objects.get(pk=user_id)
    assunto = 'Upper bound {}'.format(nome_ativo)
    msg = '{}, o valor do ativo {} passou o upper bound estabelecido, é recomendado a venda do ativo'.format(user.usuario, nome_ativo)
    enviado_de = settings.EMAIL_HOST_USER
    para_lista = [user.email,]
    send_mail(assunto,msg,enviado_de,para_lista)


def lower_bound_trigger(user_id,nome_ativo):  
    user = User.objects.get(pk=user_id)
    assunto = 'Lower bound {}'.format(nome_ativo)
    msg = '{}, o valor do ativo {} passou o lower bound estabelecido, é recomendado a compra do ativo'.format(user.usuario, nome_ativo)
    enviado_de = settings.EMAIL_HOST_USER
    para_lista = [user.email,]
    send_mail(assunto,msg,enviado_de,para_lista)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(teste15min, 'interval', minutes=1, name='clean_accounts', replace_existing=True)
    register_events(scheduler)
    scheduler.start()