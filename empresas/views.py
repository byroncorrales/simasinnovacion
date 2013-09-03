# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Empresas, MejoraEmpresas
from .forms import EmpresasForm, MejoraForm
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
    if 'tipo' in request.session:
        params['tipo'] = request.session['tipo']
    if 'rubro' in request.session:
        params['rubro'] = request.session['rubro']

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
            request.session['tipo'] = form.cleaned_data['tipo']
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
                        identificador=objeto.identificador,
                        lon=float(objeto.gps.longitude), 
                        lat=float(objeto.gps.latitude),
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

#ficha de las mejoras

def _queryset_filtrado_mejora(request):
    params = {}
    if 'zona' in request.session:
        params['empresa__zona'] = request.session['zona']
    if 'anio' in request.session:
        params['anio'] = request.session['anio']
    if 'tema_prueba' in request.session:
        params['tema_prueba'] = request.session['tema_prueba']
    if 'rubro_prueba' in request.session:
        params['rubro_prueba'] = request.session['rubro_prueba']
    if 'mercado_prueba' in request.session:
        params['mercado_prueba'] = request.session['mercado_prueba']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return MejoraEmpresas.objects.filter(**params)

def mejoras_index(request, template="empresas/mejoras.html"):
    if request.method == 'POST':
        form = MejoraForm(request.POST)
        if form.is_valid():
            request.session['zona'] = form.cleaned_data['zona']            
            request.session['anio'] = form.cleaned_data['anio']
            request.session['tema_prueba'] = form.cleaned_data['tema_prueba']
            request.session['rubro_prueba'] = form.cleaned_data['rubro_prueba']
            request.session['mercado_prueba'] = form.cleaned_data['mercado_prueba']
            request.session['bandera'] = 1
    else:
        form = MejoraForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado_mejora(request)
    else:
        con = ''
    
    return render(request, template, {'form':form,
                                      'lista_mejora':con})


def mejora_pagina(request, id, template="empresas/ficha_mejora.html"):
    mejora = get_object_or_404(MejoraEmpresas, id=id)
    return render(request, template, {'mejora':mejora})