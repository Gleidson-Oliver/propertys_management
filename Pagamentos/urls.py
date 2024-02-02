
from django.contrib import admin
from django.urls import include, path

from . import views

app_name= 'payments'

urlpatterns = [

    path('',  views.home),


]

