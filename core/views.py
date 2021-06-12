from django.shortcuts import render, redirect
from .models import Pessoa, FichaPessoa
from .forms import PessoaForm, FichaPessoaForm

def home(request):
    return render(request, 'core.html')


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

def pessoa_nova(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_pessoas')

def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/update_pessoa.html', data)


def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': pessoa})

#----------------------------------------------------------------------------------------
#TODO: terminar todos os cruds

def lista_ficha(request):
    fichas = FichaPessoa.objects.all()
    form = FichaPessoaForm()
    data = {'fichas': fichas, 'form': form}
    return render(request, 'core/lista_fichas.html', data)

def ficha_nova(request):
    form = FichaPessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_fichas')

#finalizar ficha update e ficha delete



