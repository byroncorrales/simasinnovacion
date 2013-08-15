# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import MediosFortalecimiento
from .forms import FortaForm
import json
from django.http import HttpResponse

def _queryset_filtrado(request):
    params = {}
    if 'tipo_medio' in request.session:
        params['tipo_medio'] = request.session['tipo_medio']
    if 'temas' in request.session:
        params['temas'] = request.session['temas']
    if 'grupos_metas' in request.session:
        params['grupos_metas'] = request.session['grupos_metas']
    if 'fecha' in request.session:
        params['fecha'] = request.session['fecha']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return MediosFortalecimiento.objects.filter(**params)

def fortalecimiento_index(request, template="fortalecimiento/fortalecimiento.html"):
    if request.method == 'POST':
        form = FortaForm(request.POST)
        if form.is_valid():
            request.session['tipo_medio'] = form.cleaned_data['tipo_medio']            
            request.session['temas'] = form.cleaned_data['temas']
            request.session['grupos_metas'] = form.cleaned_data['grupos_metas']
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['bandera'] = 1
    else:
        form = FortaForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado(request)
    else:
        con = ''
    
    return render(request, template, {'form':form,
                                      'lista_forta':con})

def medios_pagina(request, id, template="fortalecimiento/ficha_medios.html"):
    medios = get_object_or_404(MediosFortalecimiento, id=id)
    return render(request, template, {'medios':medios})