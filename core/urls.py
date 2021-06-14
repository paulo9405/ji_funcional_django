from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_ficha,
    pessoa_nova,
    pessoa_update,
    pessoa_delete,
    ficha_nova,
    ficha_update,
    ficha_delete,
    lista_enderecos,
    endereco_novo,
    endereco_update,
    endereco_delete,
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-nova/', pessoa_nova, name='core_pessoa_nova'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('ficha-pessoas/', lista_ficha, name='core_lista_fichas'),
    path('ficha-nova/', ficha_nova, name='core_ficha_nova'),
    path('ficha-update/<int:id>/', ficha_update, name='core_ficha_update'),
    path('ficha-delete/<int:id>/', ficha_delete, name='core_ficha_delete'),

    path('enderecos/', lista_enderecos, name='core_lista_enderecos'),
    path('endereco-novo/', endereco_novo, name='core_endereco_novo'),
    path('endereco-update/<int:id>/', endereco_update,
         name='core_endereco_update'),
    path('endereco-delete/<int:id>/', endereco_delete,
         name='core_endereco_delete'),

]


