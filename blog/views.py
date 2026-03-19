from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import date

# Create your views here.
def welcome(request):
    return HttpResponse("Bem-vindo ao meu blog!")

def eco(request, text):
    return HttpResponse(f"Você digitou {text}.")

def info(request):
    json = {
        "curso": "Django",
        "nivel": "iniciante"
    }

    return JsonResponse(json)

# Contexto que será passado para o template
def context(request):
    context = {
        "username": "Cartaxo",
        "current_date": date.today().strftime('%d/%m/%Y'),

    }

    return render(request, "blog/index.html", context)
