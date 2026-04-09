from django.db import models

# Create your models here.
class Autor(models.Model):
    # Semelhante ao Java, onde usamos @GeneratedValue(strategy = GenerationType.IDENTITY) para gerar o id automaticamente
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome
    
class Editora(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True, null=False, blank=False)
    titulo = models.CharField(max_length=20, null=False, blank=False)
    publicacao = models.DateField(null=False, blank=False)
    preco = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    estoque = models.IntegerField(null=False, blank=False)
    
    # Relacionamento 1:N com Editora
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo} - {self.isbn} - {self.preco} - {self.estoque} - {self.publicacao}'

class Publica(models.Model):
    id = models.AutoField(primary_key=True)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['livro', 'autor'], name='unique_livro_autor')
        ]

    def __str__(self):
        return f"{self.livro.titulo} - {self.autor.nome}"