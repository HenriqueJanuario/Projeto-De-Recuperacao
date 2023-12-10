from django.urls import path
from sanapp import views

urlpatterns = [
    path('',views.index,name='index'),
    
]