from django.db import models

class Produto(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, null=True)
    quantidade = models.IntegerField(null=True)
    ncm = models.CharField(max_length=8, null=True, unique=True)    
    marca = models.CharField(max_length=100, null=True)