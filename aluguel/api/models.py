from django.db import models
from django.db.models.deletion import CASCADE


class Client(models.Model):
    name = models.CharField(max_length=60, blank=False)
    email = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.name
    

class Rent(models.Model):
    date = models.DateField(blank=False, null=False)
    start_hours = models.CharField(max_length=5, blank=False, null=False)
    end_hours = models.CharField(max_length=5, blank=False, null=False)
    client = models.ForeignKey('Client', on_delete=CASCADE, related_name='rents')
    theme = models.ForeignKey('Tema', on_delete=CASCADE, related_name='rents')

    def __str__(self):
        return str(self.date) + ' ' + self.client.name + ' ' + self.theme.nome



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