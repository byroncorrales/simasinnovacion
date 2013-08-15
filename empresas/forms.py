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