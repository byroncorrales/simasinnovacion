# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Empresas
from .forms import EmpresasForm
import json
from django.http import HttpResponse

def _queryset_filtrado(request):
    params = {}
    if 'zona' in request.session:
        params['zona'] = request.session['zona']
    if 'organizacion_civil' in request.session:
        params['organizacion_civil'] = request.session['organizacion_civil']
    if 'activo' in request.session:
        params['activo'] = request.session['activo']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return Empresas.objects.filter(**params)

def empresas_index(request, template="empresas/empresas.html"):
    if request.method == 'POST':
        form = EmpresasForm(request.POST)
        if form.is_valid():
            request.session['zona'] = form.cleaned_data['zona']            
            request.session['organizacion_civil'] = form.cleaned_data['organizacion_civil']
            request.session['activo'] = form.cleaned_data['activo']
            request.session['bandera'] = 1
    else:
        form = EmpresasForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado(request)
    else:
        con = ''
    
    return render(request, template, {'form':form,
                                      'lista_empresas':con})

def empresas_pagina(request, id, template="empresas/ficha_empresa.html"):
    empresa = get_object_or_404(Empresas, id=id)
    return render(request, template, {'empresa':empresa})


def mapa_completo_empresa(request):
    if request.is_ajax():
        lista = []
        params = []
        if request.session['bandera'] == 1:
            params = _queryset_filtrado(request)
        else:
            params = Empresas.objects.all()

        for objeto in params:
            dicc = dict(nombre=objeto.nombre, 
                        id=objeto.id,
                        lon=float(objeto.gps.longitude) , 
                        lat=float(objeto.gps.latitude),
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')