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

class ServiciosForm(forms.Form):
    tipos_servicios = forms.ModelMultipleChoiceField(queryset=TiposServicio.objects.all(),
                                                required=False)
    temas_abordan = forms.ModelMultipleChoiceField(queryset=TemasAbordan.objects.all(),
                                            required=False)
    org_benefician = forms.ModelMultipleChoiceField(queryset=TiposOrganizacionBenefician.objects.all(),
                                            required=False)
    fecha = forms.ChoiceField(choices=CHOICE_FECHA, required=False)
