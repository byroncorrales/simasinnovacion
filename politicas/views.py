# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import EspacioInnovacion, IniciativaInnovacion
from .forms import EspacioForm, IniciativaForm
import json
from django.http import HttpResponse
from lugar.models import *

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

def mapa_completo_espacios(request):
    if request.is_ajax():
        lista = []
        dicc = ''
        for obj in EspacioInnovacion.objects.all():
            for objeto in obj.municipios_influye.all():
                dicc = dict(nombre=obj.nombre, 
                            id=obj.id,
                            identificador=obj.identificador,
                            lon=float(objeto.longitud), 
                            lat=float(objeto.latitud),
                        )
                lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

def espacio_pagina(request, id, template="innovacion/ficha_espacio.html"):
    espacio = get_object_or_404(EspacioInnovacion, id=id)
    return render(request, template, {'espacio':espacio})


#aca va los de iniciativa
#
def _queryset_filtrado_iniciativa(request):
    params = {}
    if 'tipo' in request.session:
        params['tipo'] = request.session['tipo']
    if 'tema' in request.session:
        params['tema'] = request.session['tema']
    if 'cobertura' in request.session:
        params['espacio__cobertura'] = request.session['cobertura']
    if 'activos' in request.session:
        params['espacio__activos'] = request.session['activos']
    
    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return IniciativaInnovacion.objects.filter(**params)


def iniciativa_index(request, template="innovacion/iniciativas.html"):
    if request.method == 'POST':
        form = IniciativaForm(request.POST)
        if form.is_valid():
            request.session['tipo'] = form.cleaned_data['tipo']
            request.session['tema'] = form.cleaned_data['tema']     
            request.session['cobertura'] = form.cleaned_data['cobertura']
            request.session['activos'] = form.cleaned_data['activos']
            request.session['bandera'] = 1
    else:
        form = IniciativaForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado_iniciativa(request)
    else:
        con = ''           

    return render(request, template, {'form':form,
                                      'lista_iniciativas':con})

def iniciativa_pagina(request, id, template="innovacion/ficha_iniciativa.html"):
    iniciativa = get_object_or_404(IniciativaInnovacion, id=id)
    return render(request, template, {'iniciativa':iniciativa})

    #===================================
    #Cambios Kronos Code

def espacio(request, template="espacio.html"):
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
                                      'listar_espacio':con})
