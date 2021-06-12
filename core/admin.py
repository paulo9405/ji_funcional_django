from django.contrib import admin
from .models import Pessoa, FichaPessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = (
        'nome', 'telefone', 'email', 'plano'
    )
#TODO: idade
class FichaPessoaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente', 'idade', 'peso', 'altura', 'imc', 'observacoes'
    )

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(FichaPessoa, FichaPessoaAdmin)

