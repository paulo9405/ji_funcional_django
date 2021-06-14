from django.shortcuts import render, redirect
from .models import (
    Pessoa,
    FichaPessoa,
    Documento,
    Endereco,

)

from .forms import (
    PessoaForm,
    FichaPessoaForm,
    DocumentoForm,
    EnderecoForm,

)


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

#------------------------------------------------------------------------------
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


def ficha_update(request, id):
    data = {}
    ficha = FichaPessoa.objects.get(id=id)
    form = FichaPessoaForm(request.POST or None, instance=ficha)
    data['ficha'] = ficha
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_fichas')
    else:
        return render(request, 'core/update_ficha.html', data)

#TODO: os delete no arquivo delete só retornam para a lista pessoas,
# tenho q colocar dado um retornar para a sua pagina, ou entao remover o botao
def ficha_delete(request, id):
    ficha = FichaPessoa.objects.get(id=id)
    if request.method == 'POST':
        ficha.delete()
        return redirect('core_lista_fichas')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': ficha})
#------------------------------------------------------------------------------

def lista_enderecos(request):
    enderecos = Endereco.objects.all()
    form = EnderecoForm()
    data = {'enderecos': enderecos, 'form': form}
    return render(request, 'core/lista_enderecos.html', data)

def endereco_novo(request):
    form = EnderecoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_enderecos')

def endereco_update(request, id):
    data = {}
    endereco = Endereco.objects.get(id=id)
    form = EnderecoForm(request.POST or None, instance=endereco)
    data['endereco'] = endereco
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_enderecos')
    else:
        return render(request, 'core/update_endereco.html', data)


def endereco_delete(request, id):
    endereco = Endereco.objects.get(id=id)
    if request.method == 'POST':
        endereco.delete()
        return redirect('core_lista_enderecos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': endereco})


#------------------------------------------------------------------------------
def lista_documentos(request):
    documentos = Documento.objects.all()
    form = DocumentoForm()
    data = {'documentos': documentos, 'form': form}
    return render(request, 'core/lista_documentos.html', data)


def documento_novo(request):
    form = DocumentoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('core_lista_documentos')


def documento_update(request, id):
    data = {}
    documento = Documento.objects.get(id=id)
    form = DocumentoForm(request.POST or None, instance=documento)
    data['documento'] = documento
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_documentos')
    else:
        return render(request, 'core/update_documento.html', data)


def documento_delete(request, id):
    documento = Documento.objects.get(id=id)
    if request.method == 'POST':
        documento.delete()
        return redirect('core_lista_documentos')
    else:
        return render(request, 'core/delete_confirm.html', {'obj': documento})