from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm


def home(request):
    return render(request, "edu/home.html")


# ---------------------------
# CRUD Autor
# ---------------------------
def autor_list(request):
    autores = Autor.objects.all().order_by("nome")
    return render(request, "edu/home.html", {"autores": autores})


def autor_create(request):
    form = AutorForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Autor cadastrado com sucesso.")
        return redirect("autor_list")
    return render(request, "edu/autor/form.html", {"form": form, "titulo": "Novo Autor"})


def autor_update(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    form = AutorForm(request.POST or None, instance=autor)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Autor atualizado com sucesso.")
        return redirect("autor_list")
    return render(request, "edu/autor/form.html", {"form": form, "titulo": "Editar Autor"})


def autor_delete(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == "POST":
        autor.delete()
        messages.success(request, "Autor removido com sucesso.")
        return redirect("autor_list")
    return render(request, "edu/autor/confirm_delete.html", {"obj": autor})


# ---------------------------
# CRUD Editora
# ---------------------------
def editora_list(request):
    editoras = Editora.objects.all().order_by("nome")
    return render(request, "edu/editora/list.html", {"editoras": editoras})


def editora_create(request):
    form = EditoraForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Editora cadastrada com sucesso.")
        return redirect("editora_list")
    return render(request, "edu/editora/form.html", {"form": form, "titulo": "Nova Editora"})


def editora_update(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    form = EditoraForm(request.POST or None, instance=editora)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Editora atualizada com sucesso.")
        return redirect("editora_list")
    return render(request, "edu/editora/form.html", {"form": form, "titulo": "Editar Editora"})


def editora_delete(request, pk):
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == "POST":
        editora.delete()
        messages.success(request, "Editora removida com sucesso.")
        return redirect("editora_list")
    return render(request, "edu/editora/confirm_delete.html", {"obj": editora})


# ---------------------------
# CRUD Livro
# ---------------------------
def livro_list(request):
    livros = Livro.objects.select_related("editora").all().order_by("titulo")
    return render(request, "edu/livro/list.html", {"livros": livros})


def livro_create(request):
    form = LivroForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Livro cadastrado com sucesso.")
        return redirect("livro_list")
    return render(request, "edu/livro/form.html", {"form": form, "titulo": "Novo Livro"})


def livro_update(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    form = LivroForm(request.POST or None, instance=livro)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Livro atualizado com sucesso.")
        return redirect("livro_list")
    return render(request, "edu/livro/form.html", {"form": form, "titulo": "Editar Livro"})


def livro_delete(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == "POST":
        livro.delete()
        messages.success(request, "Livro removido com sucesso.")
        return redirect("livro_list")
    return render(request, "edu/livro/confirm_delete.html", {"obj": livro})


# ---------------------------
# CRUD Publica (N:N Livro x Autor)
# ---------------------------
def publica_list(request):
    publicacoes = Publica.objects.select_related("livro", "autor").all().order_by("livro__titulo", "autor__nome")
    return render(request, "edu/publica/list.html", {"publicacoes": publicacoes})


def publica_create(request):
    form = PublicaForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Vínculo livro-autor cadastrado com sucesso.")
        return redirect("publica_list")
    return render(request, "edu/publica/form.html", {"form": form, "titulo": "Nova Publicação"})


def publica_update(request, pk):
    publica = get_object_or_404(Publica, pk=pk)
    form = PublicaForm(request.POST or None, instance=publica)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Vínculo livro-autor atualizado com sucesso.")
        return redirect("publica_list")
    return render(request, "edu/publica/form.html", {"form": form, "titulo": "Editar Publicação"})


def publica_delete(request, pk):
    publica = get_object_or_404(Publica, pk=pk)
    if request.method == "POST":
        publica.delete()
        messages.success(request, "Vínculo livro-autor removido com sucesso.")
        return redirect("publica_list")
    return render(request, "edu/publica/confirm_delete.html", {"obj": publica})