from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # Adicione outros campos necessários para o perfil do usuário

    def __str__(self):
        return self.username
