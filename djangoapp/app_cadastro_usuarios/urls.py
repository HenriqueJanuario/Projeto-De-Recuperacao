# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    # Adicione outras rotas de acordo com suas necessidades
]
