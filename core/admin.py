from django.contrib import admin
from .models import Pessoa, FichaPessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'telefone', 'email', 'plano_mes', 'plano_tri'
    )

class FichaPessoaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente', 'peso', 'altura', 'imc', 'data_inicio', 'observacoes'
    )

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(FichaPessoa, FichaPessoaAdmin)

