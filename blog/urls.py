from django.urls import path
from . import views

# APENAS os endpoints do app blog
urlpatterns = [
    # Endpoint que chama a função welcome quando o usuário acessar /welcome/
    path('welcome/', views.welcome, name='welcome'),

    # Endpoint que chama a função eco e que passa também um parâmetro de texto, quando o usuário acessar /eco
    path("eco/<str:text>/", views.eco),
    path("info/", views.info)
]