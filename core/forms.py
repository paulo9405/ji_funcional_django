from django.db.models import fields
from django.forms import ModelForm
from .models import Pessoa, FichaPessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class FichaPessoaForm(ModelForm):
    class Meta:
        model = FichaPessoa
        fields = '__all__'
