# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import EspacioInnovacion, IniciativaInnovacion
from .forms import EspacioForm
import json
from django.http import HttpResponse

def _queryset_filtrado(request):
    params = {}
    if 'zona' in request.session:
        params['zona'] = request.session['zona']
    if 'cobertura' in request.session:
        params['cobertura'] = request.session['cobertura']
    if 'activos' in request.session:
        params['activos'] = request.session['activos']
    if 'tipos' in request.session:
        params['tipos'] = request.session['tipos']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return EspacioInnovacion.objects.filter(**params)

def espacio_index(request, template="innovacion/innovacion.html"):
    if request.method == 'POST':
        form = EspacioForm(request.POST)
        if form.is_valid():
            request.session['zona'] = form.cleaned_data['zona']            
            request.session['cobertura'] = form.cleaned_data['cobertura']
            request.session['activos'] = form.cleaned_data['activos']
            request.session['tipos'] = form.cleaned_data['tipos']
            request.session['bandera'] = 1
    else:
        form = EspacioForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado(request)
    else:
        con = ''
    
    return render(request, template, {'form':form,
                                      'lista_espacio':con})

def espacio_pagina(request, id, template="innovacion/ficha_espacio.html"):
    espacio = get_object_or_404(EspacioInnovacion, id=id)
    return render(request, template, {'espacio':espacio})
