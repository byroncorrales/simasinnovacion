# -*- coding: utf-8 -*-

from django import forms
from .models import *

CHOICE_FECHA= (
        ('','-------'),
        (2013,2013),
        (2014,2014),
        (2015,2015),
        (2016,2016),
        (2017,2017),
    )

class FortaForm(forms.Form):
    tipo_medio = forms.ModelMultipleChoiceField(queryset=TiposMedios.objects.all(),
                                                required=False)
    temas = forms.ModelMultipleChoiceField(queryset=TemasAbordan.objects.all(),
                                            required=False)
    grupos_metas = forms.ModelMultipleChoiceField(queryset=GruposMetas.objects.all(),
                                            required=False)
    fecha = forms.ChoiceField(choices=CHOICE_FECHA, required=False)
