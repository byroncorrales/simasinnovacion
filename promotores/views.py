# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Promotor, PracticasProductivas
from empresas.models import Empresas, MejoraEmpresas
from innovacion.models import EspacioInnovacion, IniciativaInnovacion
from fortalecimiento.models import MediosFortalecimiento
from servicios.models import Servicios 
from .forms import PromotorForm, PracticaForm
import json
from django.http import HttpResponse

def inicio(request, template="inicio.html"):
    promotores = Promotor.objects.count()
    practicas = PracticasProductivas.objects.count()
    empresas = Empresas.objects.count()
    mejoras_empresa = MejoraEmpresas.objects.count()
    espacios = EspacioInnovacion.objects.count()
    iniciativas = IniciativaInnovacion.objects.count()
    fortalecimientos = MediosFortalecimiento.objects.count()
    servicios = Servicios.objects.count()

    return render(request, template, locals())

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
                        identificador=objeto.identificador,
                        lon=float(objeto.gps.longitude) , 
                        lat=float(objeto.gps.latitude),
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

#Esta mapa es el de la pagina principal al inicio del sistema

def mapa_completo_index(request):
    if request.is_ajax():
        lista = []
        for objeto in Promotor.objects.all():
            dicc = dict(nombre=objeto.nombre, 
                        id=objeto.id,
                        identificador=objeto.identificador,
                        lon=float(objeto.gps.longitude) , 
                        lat=float(objeto.gps.latitude),
                        )
            lista.append(dicc)
        for obj in Empresas.objects.all():
            dicc = dict(nombre=obj.nombre,
                        id=obj.id,
                        identificador=obj.identificador,
                        lon=float(obj.gps.longitude),
                        lat=float(obj.gps.latitude),
                        )
            lista.append(dicc)

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

#parte de la practicas del promotor

def _queryset_filtrado_practica(request):
    params = {}
    if 'zona' in request.session:
        params['promotor__zona'] = request.session['zona']
    if 'anio' in request.session:
        params['anio'] = request.session['anio']
    if 'tema_prueba' in request.session:
        params['tema_prueba'] = request.session['tema_prueba']
    if 'rubro_prueba' in request.session:
        params['rubro_prueba'] = request.session['rubro_prueba']
    if 'escala_prueba' in request.session:
        params['escala_prueba'] = request.session['escala_prueba']

    unvalid_keys = []
    for key in params:
        if not params[key]:
            unvalid_keys.append(key)
    
    for key in unvalid_keys:
        del params[key]
    
    return PracticasProductivas.objects.filter(**params)


def practicas_index(request, template="promotor/practica.html"):
    if request.method == 'POST':
        form = PracticaForm(request.POST)
        if form.is_valid():
            request.session['zona'] = form.cleaned_data['zona']
            request.session['anio'] = form.cleaned_data['anio']         
            request.session['tema_prueba'] = form.cleaned_data['tema_prueba']
            request.session['rubro_prueba'] = form.cleaned_data['rubro_prueba']
            request.session['escala_prueba'] = form.cleaned_data['escala_prueba']
            request.session['bandera'] = 1
    else:
        form = PracticaForm()
        request.session['bandera'] = 0

    if request.session['bandera'] == 1:
        con = _queryset_filtrado_practica(request)
    else:
        con = ''
    
    return render(request, template, {'form':form,
                                      'lista_practica':con})

def mapa_completo_practica(request):
    if request.is_ajax():
        lista = []
        params = []
        if request.session['bandera'] == 1:
            params = _queryset_filtrado_practica(request)
        else:
            params = PracticasProductivas.objects.all()

        for objeto in params:
            dicc = dict(nombre=objeto.nombre_prueba, 
                        id=objeto.id,
                        lon=float(objeto.promotor.gps.longitude) , 
                        lat=float(objeto.promotor.gps.latitude),
                        )
            lista.append(dicc)

        serializado = json.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')


def practica_pagina(request, id, template="promotor/ficha_practica.html"):
    practica = get_object_or_404(PracticasProductivas, id=id)
    return render(request, template, {'practica':practica})