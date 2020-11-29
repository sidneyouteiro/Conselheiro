from django.urls import path
from .views import * 


urlpatterns = [
    path('perfil/',perfil, name='perfilPage'),
    path('',home, name='homePage'),


]