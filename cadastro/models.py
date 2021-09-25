from django.db import models

# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    etapa = models.CharField(max_length=100)

    def __str__(self):
        return f'nome: {self.nome}, CPF: {self.cpf}, status: {self.etapa}'


