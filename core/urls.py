from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_ficha,
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),

    path('ficha-pessoas/', lista_ficha, name='core_lista_fichas'),
]


