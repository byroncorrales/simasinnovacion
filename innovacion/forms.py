# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.forms import ModelForm

CHOICE_COBERTURA_DOS = (
            ('', 'Cobertura'),
            (1, 'Regional'),
            (2, 'Nacional'),
            (3, 'Territorial'),
            (4, 'Municipal'),
        )

class EspacioForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    cobertura = forms.ChoiceField(choices=CHOICE_COBERTURA_DOS, 
                                  required=False, 
                                  label="Cobertura")
    activos = forms.ChoiceField(choices=[('', 'año activo'),
                                        (1, '2013'),(2, '2014'),
                                        (3, '2015'),(4, '2016')],
                                        required=False)
    tipos = forms.ModelChoiceField(queryset=TipoEspacio.objects.all().order_by('nombre'), 
                                        required=False, 
                                        empty_label="Tipos de espacios")

# def get_anios():
#     years = []
#     for en in PracticasProductivas.objects.order_by('anio').values_list('anio', flat=True):
#         years.append((en, en))
#     return list(set(years))

# class CustomChoiceField(forms.ChoiceField):

#     def __init__(self, *args, **kwargs):
#         super(CustomChoiceField, self).__init__(*args, **kwargs)
#         self.choices.insert(0, ('', 'Año'))

# class PracticaForm(forms.Form):
#     zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
#                             (3, 'Húmeda')],required=False)
#     anio = CustomChoiceField(choices=get_anios(), label="Año")
#     tema_prueba = forms.ModelChoiceField(queryset=TemasPruebas.objects.all().order_by('nombre'), 
#                             required=False, empty_label="Tema")
#     rubro_prueba = forms.ModelChoiceField(queryset=RubroPruebas.objects.all().order_by('nombre'), 
#                             required=False, empty_label="Rubro")
#     escala_prueba = forms.ModelChoiceField(queryset=EscalaPruebas.objects.all().order_by('nombre'), 
#                             required=False, empty_label="Escala")
