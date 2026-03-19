from django.urls import path
from . import views

# APENAS os endpoints do app blog
urlpatterns = [
    # Endpoint que chama a função welcome quando o usuário acessar /welcome/
    path("welcome/", views.welcome),

    # Endpoint que chama a função eco e que passa também um parâmetro de texto, quando o usuário acessar /eco
    path("eco/<str:text>/", views.eco),

    # Endpoint que retorna o json
    path("info/", views.info),

    # Endpoint para trabalhar com context/templates
    path("main/", views.context, name="main"),

    # Endpoints para redirecionar para páginas home e contact
    path("home/", views.home, name="home"),
    path("contact/<str:phone_number>/", views.contact, name="contact"),


]