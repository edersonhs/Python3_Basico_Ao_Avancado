from django.shortcuts import render
from django.http import HttpResponse


def index(request):   # Método carregado quando o /blog é acessado
    return HttpResponse('Olá mundo!')
