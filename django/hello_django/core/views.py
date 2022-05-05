from django.shortcuts import render, HttpResponse


# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<h1>Hello {nome} de {idade} anos!</h1>')

def soma(request, valor1, valor2):
    return HttpResponse(f'{valor1} + {valor2} = {valor1 + valor2}')

def subtracao(request, valor1, valor2):
    return HttpResponse(f'{valor1} - {valor2} = {valor1 - valor2}')

def multiplicacao(request, valor1, valor2):
    return HttpResponse(f'{valor1} * {valor2} = {valor1 * valor2}')

def divisao(request, valor1, valor2):
    return HttpResponse(f'{valor1} / {valor2} = {valor1 / valor2}')
