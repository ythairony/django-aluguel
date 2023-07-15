from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Tema(models.Model):
    nome = models.CharField(max_length=50)
    valor_aluguel = models.DecimalField("Valor de aluguel",max_digits=6, decimal_places=2)
    cor = models.CharField(max_length=10)
    tema = models.ManyToManyField(Item)

    def __str__(self):
        return self.nome