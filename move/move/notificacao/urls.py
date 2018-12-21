from django.urls import path
from . import views

urlpatterns = [
    path('setor/novo' , views.registrarSetor,
         name='registrarSetor')
]