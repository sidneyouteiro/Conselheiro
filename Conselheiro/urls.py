"""Conselheiro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as django_views
from conselheiro import views as usuario_views

urlpatterns = [
    path('', include('conselheiro.urls')),

    #Usuario
    path('login/', usuario_views.logon, name='loginPage'),
    path('logout/',django_views.LogoutView.as_view(template_name='template/login.html'),name='Logout'),
    path('registro/',usuario_views.registro, name='registroPage'),

    path('admin/',admin.site.urls)
]
