# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.forms import ModelForm

class PromotorForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    organizacion_civil = forms.ModelChoiceField(queryset=OrganizacionCivil.objects.all().order_by('nombre'), 
                            required=False, empty_label="Organización")
    sexo = forms.ChoiceField(choices=[('', 'sexo'),(1,'Masculino'),
                                      (2, 'Femenino')],
                                      required=False)
    activo = forms.ChoiceField(choices=[('', 'año activo'),(1, '2013'),(2, '2014'),
                                (3, '2015'),(4, '2016')], required=False)

def get_anios():
    years = []
    for en in PracticasProductivas.objects.order_by('anio').values_list('anio', flat=True):
        years.append((en, en))
    return list(set(years))

class CustomChoiceField(forms.ChoiceField):

    def __init__(self, *args, **kwargs):
        super(CustomChoiceField, self).__init__(*args, **kwargs)
        self.choices.insert(0, ('', 'Año'))

class PracticaForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    anio = CustomChoiceField(choices=get_anios(), label="Año")
    tema_prueba = forms.ModelChoiceField(queryset=TemasPruebas.objects.all().order_by('nombre'), 
                            required=False, empty_label="Tema")
    rubro_prueba = forms.ModelChoiceField(queryset=RubroPruebas.objects.all().order_by('nombre'), 
                            required=False, empty_label="Rubro")
    escala_prueba = forms.ModelChoiceField(queryset=EscalaPruebas.objects.all().order_by('nombre'), 
                            required=False, empty_label="Escala")
