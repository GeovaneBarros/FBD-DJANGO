from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    sexo = models.CharField(max_length=10)
    nome_usuario = models.CharField(max_length=15, unique=True)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.nome_usuario)

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=400)
    marca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.nome)

class Avaliacao(models.Model):
    produtoFK = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nota = models.IntegerField()
    coment = models.CharField(max_length=300)
    pessoaFK = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.pessoaFK.nome_usuario, self.produtoFK.nome)