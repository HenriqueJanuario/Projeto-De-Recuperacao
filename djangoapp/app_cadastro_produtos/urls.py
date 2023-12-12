"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app_cadastro_produtos import views


urlpatterns = [
    path('', views.home_produtos, name="home_produtos"),
    # produtos.com/cadastro
    path('cadastro/', views.cadastro_produtos, name="cadastro_produtos"),
    # produtos.com/listagem_cliente
    path('listagem_produtos/', views.listagem_produtos, name='listagem_produtos'),
    # produtos.com/editar
    path('editar/<int:produtos_id>/', views.editar_produtos, name="editar_produtos"),
    # produtos.com/excluir
    path('delete_produtos/<int:produtos_id>/',views.delete_produtos, name='delete_produtos'),
]
