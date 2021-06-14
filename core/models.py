import decimal
from builtins import max

from django.db import models
from django.db.models.deletion import CASCADE
import datetime
import math

#TODO: terminar todos os cruds
class Plano(models.Model):
    tipo = models.CharField(max_length=100)
    valor = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return self.tipo + ': ' + str(self.valor)



class Pessoa(models.Model):
    nome = models.CharField(u'Nome', max_length=100)
    telefone = models.CharField(u'Telefone', max_length=50)
    email = models.EmailField(u'Email', max_length=100,)
    data_nascimento = models.DateField(u'data de nascimento', auto_now=False)
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True)
    horario_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ultima_vez_modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome


class Documento(models.Model):
    TIPO = (
        ('RG', 'Carteira de Identidade (RG)'),
        ('CPF', 'Cadastro Unico de Pessoa Fisica (CPF)'),
        ('PP', 'Passaporte')
    )
    tipo = models.CharField(max_length=3, choices=TIPO)
    numero = models.CharField(max_length=50)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, help_text='Pessoa')

    def __str__(self):
        return 'Documentos de ' +''+ str(self.pessoa)


class Endereco(models.Model):
    proprietario = models.ForeignKey(Pessoa, on_delete=models.CASCADE, null=True, blank=True)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=6, null=True)
    bairro = models.CharField(max_length=50, null=True)
    cidade = models.CharField(max_length=50, null=True)
    estado = models.CharField(max_length=50, null=True)
    pais = models.CharField(max_length=50, null=True)
    def __str__(self):
        #return str(self.rua) + ' - ' + str(self.bairro)
        return 'endereço de ' +''+ str(self.proprietario)


class FichaPessoa(models.Model):
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
        return str(self.cliente)












