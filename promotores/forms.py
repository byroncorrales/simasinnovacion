# -*- coding: utf-8 -*-

from django import forms
from .models import *
from django.forms import ModelForm

class PromotorForm(forms.Form):
    zona = forms.ChoiceField(choices=[('', '----------'),(1, 'Seca'),(2, 'Alta'),
                            (3, 'Húmeda')],required=False)
    organizacion_civil = forms.ModelChoiceField(queryset=OrganizacionCivil.objects.all().order_by('nombre'), 
                            required=False)
    sexo = forms.ChoiceField(choices=[('', '----------'),(1,'Masculino'),
                                      (2, 'Femenino')],
                                      required=False)
    activo = forms.ChoiceField(choices=[('', '----------'),(1, '2013'),(2, '2014'),
                                (3, '2015'),(4, '2016')], required=False)

    # class Meta:
    #     model = Promotor
    #     fields = ('zona','organizacion_civil','sexo','activo',)