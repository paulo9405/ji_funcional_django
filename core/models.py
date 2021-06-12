from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import math

class Pessoa(models.Model):
    PLANO = (
        ('M', 'Mensal R$ 50,00'),
        ('T', 'Trimestral R$ 130,00'),
    )
    nome = models.CharField(u'Nome', max_length=100)
    telefone = models.CharField(u'Telefone', max_length=50)
    email = models.EmailField(u'Email', max_length=100,)
    endereço = models.CharField(u'Endereço', max_length=100)
    data_nascimento = models.DateField('data de nascimento', auto_now=False)
    plano = models.CharField(max_length=1, choices=PLANO)

    def __str__(self):
        return self.nome


class FichaPessoa(models.Model):
    #TODO: colocar em um arquivo para exportar pq ta feio, nao sei como faz, mas sei q da pra fazer!
    SEXO = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    )

    cliente = models.ForeignKey(Pessoa, on_delete=CASCADE)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO)
    peso = models.DecimalField(max_digits=6, decimal_places=3)
    altura= models.DecimalField(max_digits=3, decimal_places=2)
    imc = models.DecimalField(max_digits=4, decimal_places=2)
    data_inicio = models.DateField('Inicio das atividades', auto_now=False)
    observacoes = models.TextField()


    def __str__(self):
        return str(self.cliente) + ' - ' + str(self.peso)












