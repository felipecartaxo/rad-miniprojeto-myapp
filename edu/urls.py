from django.urls import path
from . import views

# APENAS os endpoints do app edu
urlpatterns = [
    # Endpoint que chama a função test quando o usuário acessar /test/
    path("test/", views.test),
]