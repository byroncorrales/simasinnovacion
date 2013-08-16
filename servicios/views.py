# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Servicios
from .forms import ServiciosForm
import json
from django.http import HttpResponse

def _queryset_filtrado(request):
    params = {}
    if 'tipos_servicios' in request.session:
        params['tipos_servicios'] = request.session['tipos_servicios']
    if 'temas_abordan' in request.session:
        params['temas_abordan'] = request.session['temas_abordan']
    if 'org_benefician' in request.session:
        params['org_benefician'] = request.session['org_benefician']
    if 'fecha' in request.session:
        params['fecha'] = request.session['fecha']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return Servicios.objects.filter(**params)

def servicios_index(request, template="servicios/servicios.html"):
    if request.method == 'POST':
        form = ServiciosForm(request.POST)
        if form.is_valid():
            request.session['tipos_servicios'] = form.cleaned_data['tipos_servicios']            
            request.session['temas_abordan'] = form.cleaned_data['temas_abordan']
            request.session['org_benefician'] = form.cleaned_data['org_benefician']
            request.session['fecha'] = form.cleaned_data['fecha']
            request.session['bandera'] = 1
    else:
        form = ServiciosForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado(request)
    else:
        con = ''
    
    return render(request, template, {'form':form,
                                      'lista_servicios':con})

def servicios_pagina(request, id, template="servicios/ficha_servicios.html"):
    servicio = get_object_or_404(Servicios, id=id)
    return render(request, template, {'servicio':servicio})