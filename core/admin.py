from django.contrib import admin
from .models import (
    Pessoa,
    FichaPessoa,
    Plano,
    Endereco,
    Documento
)

class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'telefone', 'email', 'plano'
    )


class FichaPessoaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente', 'idade','sexo', 'peso', 'altura', 'imc', 'data_inicio', 'observacoes'
    )


class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        'pessoa', 'tipo', 'numero',
    )


class EnderecoAdmin(admin.ModelAdmin):
    list_display = (
        'proprietario', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'pais'
    )

class PlanoAdmin(admin.ModelAdmin):
    list_display = (
        'tipo', 'valor'
    )

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(FichaPessoa, FichaPessoaAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Endereco, EnderecoAdmin)
admin.site.register(Plano, PlanoAdmin)
