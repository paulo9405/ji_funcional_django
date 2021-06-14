from django.forms import ModelForm
from .models import (
    Pessoa,
    FichaPessoa,
    Documento,
    Endereco,
    Plano,
)

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class FichaPessoaForm(ModelForm):
    class Meta:
        model = FichaPessoa
        fields = '__all__'

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class PlanoForm(ModelForm):
    class Meta:
        model = Plano
        fields = '__all__'
