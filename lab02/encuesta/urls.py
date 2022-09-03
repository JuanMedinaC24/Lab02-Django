from django.urls import path

from . import views

app_name='encuesta'

urlpatterns = [
    #path('', views.index,name='index'),
    #path('enviar', views.enviar,name='enviar'),
    
    #path('', views.indexmatematico,name='indexmatematico'),
    #path('enviar2', views.enviar2,name='enviar2'),
    
    path('', views.indexcilindro,name='indexcilindro'),
    path('calcular', views.calcular,name='calcular'),
   
]