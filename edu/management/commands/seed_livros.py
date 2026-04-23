from decimal import Decimal
import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from edu.models import Livro, Editora


class Command(BaseCommand):
    help = "Gera registros de livros no banco (default: 100)."

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            type=int,
            default=100,
            help="Quantidade de livros a criar (padrão: 100).",
        )

    def handle(self, *args, **options):
        total = options["total"]
        fake = Faker("pt_BR")

        # Garante editoras para vincular os livros
        editoras = list(Editora.objects.all())
        if not editoras:
            editoras = [
                Editora.objects.create(nome=fake.unique.company())
                for _ in range(10)
            ]
            self.stdout.write(self.style.WARNING("Editoras não encontradas. 10 editoras foram criadas automaticamente."))

        criados = 0
        tentativas = 0
        max_tentativas = total * 10  # evita loop infinito por colisão de ISBN único

        while criados < total and tentativas < max_tentativas:
            tentativas += 1

            isbn = fake.isbn13(separator="")
            titulo = fake.sentence(nb_words=4).replace(".", "")[:20]  # respeita max_length=20
            publicacao = fake.date_between(start_date="-30y", end_date="today")
            preco = Decimal(str(round(random.uniform(19.9, 299.9), 2)))
            estoque = random.randint(0, 500)
            editora = random.choice(editoras)

            # Evita erro por unique no ISBN
            if Livro.objects.filter(isbn=isbn).exists():
                continue

            Livro.objects.create(
                isbn=isbn,
                titulo=titulo,
                publicacao=publicacao,
                preco=preco,
                estoque=estoque,
                editora=editora,
            )
            criados += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Concluído: {criados} livros criados (solicitado: {total})."
            )
        )

        if criados < total:
            self.stdout.write(
                self.style.WARNING(
                    "Nem todos os livros foram criados devido a colisões de dados únicos (ISBN)."
                )
            )