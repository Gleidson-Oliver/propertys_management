
from django.contrib import admin
from django.urls import include, path

from . import views

app_name= 'rental'

urlpatterns = [

  
    path('',  views.home),
    path('pagamentos/',  include('Pagamentos.urls'))


]

