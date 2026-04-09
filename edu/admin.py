from django.contrib import admin
from .models import Autor, Editora, Livro, Publica

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    search_fields = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id','titulo','isbn','preco','estoque','publicacao','editora')
    search_fields = ('titulo','isbn')
    list_filter = ('editora',)

@admin.register(Publica)
class PublicaAdmin(admin.ModelAdmin):
    list_display = ('id','livro','autor')
    search_fields = ('livro__titulo','autor__nome')
