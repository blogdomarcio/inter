from django.db import models

# Create your models here.


class Estilo(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)
    descricao = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='imagens/estilo', null=True, blank=True)

    def __str__(self):
        return self.titulo

class Quarto(models.Model):
    estilo = models.ForeignKey(Estilo, null=False)
    titulo = models.CharField(max_length=100, unique=True, null=False)
    imagem = models.ImageField(upload_to='imagens/quarto', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.titulo) + ' - ' + str(self.estilo)

class Cozinha(models.Model):
    estilo = models.ForeignKey(Estilo, null=False)
    titulo = models.CharField(max_length=100, unique=True, null=False)
    imagem = models.ImageField(upload_to='imagens/cozinha', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Sala(models.Model):
    estilo = models.ForeignKey(Estilo, null=False)
    titulo = models.CharField(max_length=100, unique=True, null=False)
    imagem = models.ImageField(upload_to='imagens/sala', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.titulo) + ' - ' + str(self.estilo)

class Banheiro(models.Model):
    estilo = models.ForeignKey(Estilo, null=False)
    titulo = models.CharField(max_length=100, unique=True, null=False)
    imagem = models.ImageField(upload_to='imagens/banheiro', null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
