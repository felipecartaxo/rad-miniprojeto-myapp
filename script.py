import os
import django
from decimal import Decimal
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
django.setup()

from edu.models import Autor, Editora, Livro, Publica

def create_sample():
    e, _ = Editora.objects.get_or_create(nome='Editora Exemplo')
    a, _ = Autor.objects.get_or_create(nome='Agatha Exemplo')

    livro, created = Livro.objects.get_or_create(
        isbn='9781111111111',
        defaults={
            'titulo': 'Livro Exemplo',
            'publicacao': date(2022, 1, 1),
            'preco': Decimal('29.90'),
            'estoque': 10,
            'editora': e
        }
    )
    if created:
        Publica.objects.create(livro=livro, autor=a)
    print('Criado:', livro)

def list_livros():
    for l in Livro.objects.all():
        print(l)

def update_preco(isbn, novo_preco):
    try:
        l = Livro.objects.get(isbn=isbn)
        l.preco = Decimal(novo_preco)
        l.save()
        print('Atualizado:', l)
    except Livro.DoesNotExist:
        print('Livro não encontrado:', isbn)

def delete_livro(isbn):
    qs = Livro.objects.filter(isbn=isbn)
    if qs.exists():
        qs.delete()
        print('Deletado livro com ISBN', isbn)
    else:
        print('Nenhum livro com ISBN', isbn)

if __name__ == '__main__':
    create_sample()
    list_livros()
    update_preco('9781111111111', '34.90')
    # delete_livro('9781111111111')