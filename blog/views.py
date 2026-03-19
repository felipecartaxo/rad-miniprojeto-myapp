from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from datetime import datetime

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
        "current_date": datetime.now().strftime('%d/%m/%Y'),
        "is_logged_in": True,
        "roles" : [
            'admin',
            'user'
        ],
        "products": [
            {"name": "Caneca", "price": 19.90},
            {"name": "Camiseta", "price": 39.90},
            {"name": "Adesivo", "price": 4.50},
        ],
    }

    return render(request, "blog/index.html", context)
