from django.shortcuts import render
from .models import Pessoa, FichaPessoa
from .forms import PessoaForm, FichaPessoaForm

def home(request):
    return render(request, 'core.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()


    return render(request, 'core/lista_pessoas.html', {'pessoas': pessoas})

#----------------------------------------------------------------------------------------

def lista_ficha(request):
    fichas = FichaPessoa.objects.all()

    return render(request, 'core/lista_fichas.html', {'fichas': fichas})


