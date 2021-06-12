from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_ficha,
    pessoa_nova,
    pessoa_update,
    pessoa_delete,
    ficha_nova
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoa-nova/', pessoa_nova, name='core_pessoa_nova'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('ficha-pessoas/', lista_ficha, name='core_lista_fichas'),
    path('ficha-nova/', ficha_nova, name='core_ficha_nova'),

]


