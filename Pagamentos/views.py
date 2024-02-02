from django.shortcuts import render
from django.views.generic import ListView


def home(request):
    return render(request, 'alugueis/pages/home.html')



