# -*- coding: utf-8 -*-

from django import forms
from .models import *
from promotores.models import OrganizacionCivil

class EmpresasForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    organizacion_civil = forms.ModelChoiceField(queryset=OrganizacionCivil.objects.all().order_by('nombre'), 
                            required=False, empty_label="Organización")
    activo = forms.ChoiceField(choices=[('', 'año activo'),(1, '2013'),(2, '2014'),
                                (3, '2015'),(4, '2016')], required=False)
    tipo = forms.ModelChoiceField(queryset=TipoEmpresa.objects.all().order_by('nombre'), 
                            required=False, empty_label="Tipo empresa")
    rubro = forms.ModelChoiceField(queryset=Rubros.objects.all().order_by('nombre'), 
                            required=False, empty_label="Rubros")

def get_anios():
    years = []
    for en in MejoraEmpresas.objects.order_by('anio').values_list('anio', flat=True):
        years.append((en, en))
    return list(set(years))

class CustomChoiceField(forms.ChoiceField):

    def __init__(self, *args, **kwargs):
        super(CustomChoiceField, self).__init__(*args, **kwargs)
        self.choices.insert(0, ('', 'Año'))

class MejoraForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', 'zona'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    anio = CustomChoiceField(choices=get_anios(),required=False, label="Año")
    tema_prueba = forms.ModelChoiceField(queryset=TemasEmpresa.objects.all().order_by('nombre'), 
                            required=False, empty_label="Tema")
    rubro_prueba = forms.ModelChoiceField(queryset=Rubros.objects.all().order_by('nombre'), 
                            required=False, empty_label="Rubro")
    mercado_prueba = forms.ModelChoiceField(queryset=Mercados.objects.all().order_by('nombre'), 
                            required=False, empty_label="Mercados")