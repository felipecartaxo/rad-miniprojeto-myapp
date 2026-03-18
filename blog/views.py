from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

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
