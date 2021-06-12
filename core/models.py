from django.db import models
from django.db.models.deletion import CASCADE
import math

class Pessoa(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    telefone = models.CharField(u'Telefone', max_length=50)
    email = models.EmailField(u'Email', max_length=100,)
    endereço = models.CharField(u'Endereço', max_length=100)

    plano_mes = models.BooleanField(
        u'Plano Mensal R$ 50,00', null=True
    )

    plano_tri = models.BooleanField(
        u'Plano Trimestral R$ 130,00', null=True
    )

    def __str__(self):
        return self.nome


class FichaPessoa(models.Model):
    cliente = models.ForeignKey(Pessoa, on_delete=CASCADE)

    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura= models.DecimalField(max_digits=3, decimal_places=2)
    imc = models.DecimalField(max_digits=4, decimal_places=2)
    data_inicio = models.DateField()
    observacoes = models.TextField()

    def __str__(self):
        return str(self.cliente) + ' - ' + str(self.peso)











