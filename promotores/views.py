# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from .models import Promotor, PracticasProductivas, EscalaPruebas
from empresas.models import Empresas, MejoraEmpresas, TipoEmpresa, TemasEmpresa, Mercados
from politicas.models import EspacioInnovacion, IniciativaInnovacion, TipoEspacio, \
                             PapelSimas, TipoIniciativa
from fortalecimiento.models import MediosFortalecimiento, TiposMedios
from servicios.models import Servicios, TiposServicio
from .forms import PromotorForm, PracticaForm
import json
from django.http import HttpResponse

def inicio(request, template="inicio.html"):
    choice_zonas=((1, 'Seca'),(2, 'Alta'),(3, 'Húmeda'),)
    promotores = Promotor.objects.count()
    #salidas graficos promotores por sexo
    h_promotor = Promotor.objects.filter(sexo=1).count()
    m_promotor = Promotor.objects.filter(sexo=2).count()
    #salidas graficos promotor por zona
    seca = Promotor.objects.filter(zona=1).count()
    alta = Promotor.objects.filter(zona=2).count()
    humeda = Promotor.objects.filter(zona=3).count()
    #salidas grafico de practicas
    practicas = PracticasProductivas.objects.count()

    #practicas por escala
    escala = []
    for obj in EscalaPruebas.objects.all():
        escala.append([obj.nombre,PracticasProductivas.objects.filter(escala_prueba=obj).count()])
    #numero de practicas por años
    years = []
    for en in PracticasProductivas.objects.order_by('anio').values_list('anio', flat=True):
        years.append(en)
    lista_years = list(set(years))
    numero_practica = []
    for year in lista_years:
        a = PracticasProductivas.objects.filter(anio=year).count()
        numero_practica.append([year,a])

    #salidas graficas sobre empresas
    empresas = Empresas.objects.count()
    #conteo de tipos de empresas registradas
    tipo_empresas = []
    for obj in TipoEmpresa.objects.all():
        tipo_empresas.append([obj.nombre,Empresas.objects.filter(tipo=obj).count()])
    #conteo de las empresas por zonas
    lista_empresas_zonas = []
    for obj in choice_zonas:
        lista_empresas_zonas.append([str(obj[1]), Empresas.objects.filter(zona=obj[0]).count()])
    
    #graficos de las mejoras de las empresas
    mejoras_empresa = MejoraEmpresas.objects.count()
    #grafica de los temas de mejoras en las empresas
    lista_mejora_empresa = []
    for obj in TemasEmpresa.objects.all():
        lista_mejora_empresa.append([obj.nombre, 
                                    MejoraEmpresas.objects.filter(tema_prueba=obj).count()])
    
    #grafico de los mercados de las pruebas sobre mejora de las empresas
    lista_mercados = []
    for obj in Mercados.objects.all():
        lista_mercados.append([obj.nombre, 
                               MejoraEmpresas.objects.filter(mercado_prueba=obj).count()])

    #graficos de los espacios
    espacios = EspacioInnovacion.objects.count()
    #graficos de tipos de espacios
    lista_espacios = []
    for obj in TipoEspacio.objects.all():
        lista_espacios.append([obj.nombre, 
                             EspacioInnovacion.objects.filter(tipos=obj).count()])
    #grafico de papel de simas
    lista_papel_simas = []
    for obj in PapelSimas.objects.all():
        lista_papel_simas.append([obj.nombre, 
                                 EspacioInnovacion.objects.filter(papel=obj).count()])
    #graficos de las iniciativas politicas
    iniciativas = IniciativaInnovacion.objects.count()
    #grafico de tipos de iniciativas
    lista_iniciativas = []
    for obj in TipoIniciativa.objects.all():
        lista_iniciativas.append([obj.nombre,
                                 IniciativaInnovacion.objects.filter(tipo=obj).count()])
    #grafico de numero de iniciativas por años
    lista_years = []
    for en in IniciativaInnovacion.objects.order_by('anio').values_list('anio', flat=True):
        lista_years.append(en)
    iniciativa_years = list(set(lista_years))
    numero_iniciativa = []
    for year in iniciativa_years:
        a = IniciativaInnovacion.objects.filter(anio=year).count()
        numero_iniciativa.append([year,a])

    #graficos de fortalecimiento 
    fortalecimientos = MediosFortalecimiento.objects.count()
    tipo_medio = []
    for obj in TiposMedios.objects.all():
        tipo_medio.append([obj.nombre, 
                           MediosFortalecimiento.objects.filter(tipo_medio=obj).count()])
    simas_fotalece = []
    for obj in PapelSimas.objects.all():
        simas_fotalece.append([obj.nombre, 
                               MediosFortalecimiento.objects.filter(papel_simas=obj).count()])

    #gráficos de los servicios
    servicios = Servicios.objects.count()
    #grafico tipos de servicios
    tipo_servicios = []
    for obj in TiposServicio.objects.all():
        tipo_servicios.append([obj.nombre, 
                              Servicios.objects.filter(tipos_servicios=obj).count()])

    #graficos de servicios por año
    servicios_anios = []
    anios = []
    for en in Servicios.objects.order_by('fecha').values_list('fecha', flat=True):
        anios.append(en)
    servicios_anios = list(set(anios))
    numero_servicios = []
    for year in servicios_anios:
        a = Servicios.objects.filter(fecha=year).count()
        numero_servicios.append([year,a])


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


    #Cambios elaborados por el equipo de Kronos Code

def gpromotor(request, template="gpromotor.html"):
    choice_zonas=((1, 'Seca'),(2, 'Alta'),(3, 'Húmeda'),)
    promotores = Promotor.objects.count()
    #salidas graficos promotores por sexo
    h_promotor = Promotor.objects.filter(sexo=1).count()
    m_promotor = Promotor.objects.filter(sexo=2).count()
    #salidas graficos promotor por zona
    seca = Promotor.objects.filter(zona=1).count()
    alta = Promotor.objects.filter(zona=2).count()
    humeda = Promotor.objects.filter(zona=3).count()
    #salidas grafico de practicas
    practicas = PracticasProductivas.objects.count()

    #practicas por escala
    escala = []
    for obj in EscalaPruebas.objects.all():
        escala.append([obj.nombre,PracticasProductivas.objects.filter(escala_prueba=obj).count()])
    #numero de practicas por años
    years = []
    for en in PracticasProductivas.objects.order_by('anio').values_list('anio', flat=True):
        years.append(en)
    lista_years = list(set(years))
    numero_practica = []
    for year in lista_years:
        a = PracticasProductivas.objects.filter(anio=year).count()
        numero_practica.append([year,a])
    return render(request,template, locals())


def gempresas(request, template="gempresas.html"):
    choice_zonas=((1, 'Seca'),(2, 'Alta'),(3, 'Húmeda'),)
     #salidas graficas sobre empresas
    empresas = Empresas.objects.count()
    #conteo de tipos de empresas registradas
    tipo_empresas = []
    for obj in TipoEmpresa.objects.all():
        tipo_empresas.append([obj.nombre,Empresas.objects.filter(tipo=obj).count()])
    #conteo de las empresas por zonas
    lista_empresas_zonas = []
    for obj in choice_zonas:
        lista_empresas_zonas.append([str(obj[1]), Empresas.objects.filter(zona=obj[0]).count()])
    
    #graficos de las mejoras de las empresas
    mejoras_empresa = MejoraEmpresas.objects.count()
    #grafica de los temas de mejoras en las empresas
    lista_mejora_empresa = []
    for obj in TemasEmpresa.objects.all():
        lista_mejora_empresa.append([obj.nombre, 
                                    MejoraEmpresas.objects.filter(tema_prueba=obj).count()])
    
    #grafico de los mercados de las pruebas sobre mejora de las empresas
    lista_mercados = []
    for obj in Mercados.objects.all():
        lista_mercados.append([obj.nombre, 
                               MejoraEmpresas.objects.filter(mercado_prueba=obj).count()])
    return render(request, template, locals())

def gespacios(request, template="gespacios.html"):
    choice_zonas=((1, 'Seca'),(2, 'Alta'),(3,'Húmeda'),)
    #graficos de los espacios
    espacios = EspacioInnovacion.objects.count()
    #graficos de tipos de espacios
    lista_espacios = []
    for obj in TipoEspacio.objects.all():
        lista_espacios.append([obj.nombre, 
                             EspacioInnovacion.objects.filter(tipos=obj).count()])
    #grafico de papel de simas
    lista_papel_simas = []
    for obj in PapelSimas.objects.all():
        lista_papel_simas.append([obj.nombre, 
                                 EspacioInnovacion.objects.filter(papel=obj).count()])
    #graficos de las iniciativas politicas
    iniciativas = IniciativaInnovacion.objects.count()
    #grafico de tipos de iniciativas
    lista_iniciativas = []
    for obj in TipoIniciativa.objects.all():
        lista_iniciativas.append([obj.nombre,
                                 IniciativaInnovacion.objects.filter(tipo=obj).count()])
    #grafico de numero de iniciativas por años
    lista_years = []
    for en in IniciativaInnovacion.objects.order_by('anio').values_list('anio', flat=True):
        lista_years.append(en)
    iniciativa_years = list(set(lista_years))
    numero_iniciativa = []
    for year in iniciativa_years:
        a = IniciativaInnovacion.objects.filter(anio=year).count()
        numero_iniciativa.append([year,a])
    return render(request, template, locals())

def gservicios(request, template="gservicios.html"):    
    choice_zonas=((1, 'Seca'),(2, 'Alta'),(3,'Húmeda'),)
    #graficos de fortalecimiento 
    fortalecimientos = MediosFortalecimiento.objects.count()
    tipo_medio = []
    for obj in TiposMedios.objects.all():
        tipo_medio.append([obj.nombre, 
                           MediosFortalecimiento.objects.filter(tipo_medio=obj).count()])
    simas_fotalece = []
    for obj in PapelSimas.objects.all():
        simas_fotalece.append([obj.nombre, 
                               MediosFortalecimiento.objects.filter(papel_simas=obj).count()])

    #gráficos de los servicios
    servicios = Servicios.objects.count()
    #grafico tipos de servicios
    tipo_servicios = []
    for obj in TiposServicio.objects.all():
        tipo_servicios.append([obj.nombre, 
                              Servicios.objects.filter(tipos_servicios=obj).count()])

    #graficos de servicios por año
    servicios_anios = []
    anios = []
    for en in Servicios.objects.order_by('fecha').values_list('fecha', flat=True):
        anios.append(en)
    servicios_anios = list(set(anios))
    numero_servicios = []
    for year in servicios_anios:
        a = Servicios.objects.filter(fecha=year).count()
        numero_servicios.append([year,a])


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


def promotor(request, template="promotores.html"):
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
                                      'listar_promotor':con})

def fpromotor(request, id, template="fpromotor.html"):
    fpromotor = get_object_or_404(Promotor, id=id)
    year = request.GET.get('year', None)
    practicas_productivas_queryset = fpromotor.practicasproductivas_set.all()

    if year:
        practicas_productivas_queryset = practicas_productivas_queryset.filter(fecha_prueba__year=year)

    return render(request, template, locals())

def prueba(request, template="prueba.html"):
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
                                      'listar_prueba':con})

def fprueba(request, id, template="fprueba.html"):
    fprueba = get_object_or_404(PracticasProductivas, id=id)
    return render(request, template, {'fprueba':fprueba})
