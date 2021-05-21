from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    nome = models.CharField()

class Ativo(models.Model):
    pass