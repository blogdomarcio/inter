from django.db import models

# Create your models here.

class Banheiro(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)
    foto = models.ImageField(upload_to='banheiros', null=True, blank=True)
    descricao = models.TextField(null=True)

    def __str__(self):
        return self.titulo

class Quarto(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)
    foto = models.ImageField(upload_to='quarto', null=True, blank=True)
    descricao = models.TextField(null=True)

class Cozinha(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)
    foto = models.ImageField(upload_to='cozinha', null=True, blank=True)
    descricao = models.TextField(null=True)

class Sala(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)
    foto = models.ImageField(upload_to='sala', null=True, blank=True)
    descricao = models.TextField(null=True)

