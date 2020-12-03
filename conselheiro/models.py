from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    periodo = models.DurationField(null=True,blank=True)

class Tracking(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_ativo = models.CharField(max_length=15)
    upper_bound = models.DecimalField(max_digits=16,decimal_places=2)
    lower_bound = models.DecimalField(max_digits=16,decimal_places=2)
    periodicidade = models.DurationField()

    def __unicode__(self):
        return u"%s" % self.user

class Ativo(models.Model):
    nome_ativo = models.CharField(max_length=15)
    valor = models.DecimalField(max_digits=16,decimal_places=3)
    timestamp = models.DateTimeField(default=timezone.now)