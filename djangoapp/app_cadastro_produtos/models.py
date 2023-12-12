from django.db import models

class Produtos(models.Model):
    id_produtos = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=20, null=False) 
    valor = models.IntegerField(null=False) 
    quantidade = models.CharField(max_length=11, null=False) 
    foto = models.ImageField(upload_to='usuarios_fotos/', null=True, blank=True)
    objects = models.Manager()
