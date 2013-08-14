# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Promotor, PracticasProductivas
from .forms import PromotorForm
import json
from django.http import HttpResponse

def _queryset_filtrado(request):
    params = {}
    if 'zona' in request.session:
        params['zona'] = request.session['zona']
    if 'organizacion_civil' in request.session:
        params['organizacion_civil'] = request.session['organizacion_civil']
    if 'sexo' in request.session:
        params['sexo'] = request.session['sexo']
    if 'activo' in request.session:
        params['activo'] = request.session['activo']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return Promotor.objects.filter(**params)


def promotor_index(request, template="promotor/promotor.html"):
    if request.method == 'POST':
        form = PromotorForm(request.POST)
        if form.is_valid():
            request.session['zona'] = form.cleaned_data['zona']            
            request.session['organizacion_civil'] = form.cleaned_data['organizacion_civil']
            request.session['sexo'] = form.cleaned_data['sexo']
            request.session['activo'] = form.cleaned_data['activo']
            request.session['bandera'] = 1
    else:
        form = PromotorForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado(request)
    else:
        con = ''
    
    return render(request, template, {'form':form,
                                      'lista_promotor':con})

def promotor_pagina(request, id, template="promotor/ficha_promotor.html"):
    promotor = get_object_or_404(Promotor, id=id)
    return render(request, template, {'promotor':promotor})


def mapa_completo(request):
    if request.is_ajax():
        lista = []
        params = []
        if request.session['bandera'] == 1:
            params = _queryset_filtrado(request)
        else:
            params = Promotor.objects.all()

        for objeto in params:
            dicc = dict(nombre=objeto.nombre, 
                        id=objeto.id,
                        lon=float(objeto.gps.longitude) , 
                        lat=float(objeto.gps.latitude),
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

def mapa_completo_index(request):
    if request.is_ajax():
        lista = []
        for objeto in Promotor.objects.all():
            dicc = dict(nombre=objeto.nombre, 
                        id=objeto.id,
                        lon=float(objeto.gps.longitude) , 
                        lat=float(objeto.gps.latitude),
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

#parte de la practicas del promotor

def practica_pagina(request, id, template="promotor/ficha_practica.html"):
    practica = get_object_or_404(PracticasProductivas, id=id)
    return render(request, template, {'practica':practica})