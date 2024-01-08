from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Sousadmins(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50, verbose_name='Nom')
    prenom = models.CharField(max_length=50, verbose_name='Prénom')
    email = models.EmailField(verbose_name='Email')









