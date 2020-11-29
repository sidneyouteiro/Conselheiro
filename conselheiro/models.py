from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    periodo = models.DurationField(null=True,blank=True)
    def get_(self):
        pass
class Ativos(models.Model):
    nome = models.CharField(max_length=10)
    usuarios = models.ManyToManyField(User)
    preco = models.DecimalField(max_digits=16,decimal_places=2)

class Tracking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ativo = models.ForeignKey(Ativos, on_delete=models.CASCADE)
    upper_bound = models.DecimalField(max_digits=16,decimal_places=2)
    lower_bound = models.DecimalField(max_digits=16,decimal_places=2)
    