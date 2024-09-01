from django.db import models

class Testemunho(models.Model):
    nome = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    foto = models.FileField(upload_to="imagem/")
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Equipe(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    foto = models.FileField(upload_to="imagem/")
    descricao = models.TextField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.FileField(upload_to="imagem/")


    def __str__(self):
        return self.nome

class Contactar(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    descricao = models.TextField()


    def __str__(self):
        return self.nome