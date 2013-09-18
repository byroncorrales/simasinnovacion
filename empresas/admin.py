from django.contrib import admin
from .models import *

class RubrosPrincipalesInlines(admin.TabularInline):
    model = RubrosPrincipales
    extra = 1
    max_num = 3

class ActividadEmpresarialInlines(admin.TabularInline):
    model = ActividadEmpresarial
    extra = 1
    max_num = 7

class MercadosRubrosInlines(admin.TabularInline):
    model = MercadosRubros
    extra = 1
    max_num = 7

class CompradoresRubrosInlines(admin.TabularInline):
    model = CompradoresRubros
    extra = 1
    max_num = 7

class CertificacionesRubrosInlines(admin.TabularInline):
    model = CertificacionesRubros
    extra = 1
    max_num = 7

class FotosActividadEmpresarialInlines(admin.TabularInline):
    model = FotosActividadEmpresarial
    extra = 1

class MejoraEmpresaInline(admin.TabularInline):
    model = MejoraEmpresas
    fields = ('nombre_mejora','fecha_prueba','tema_prueba','rubro_prueba','mercado_prueba')
    extra = 1

class EmpresasAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (('nombre', 'tipo', 'activo'),
                        ('formado_empresa','contacto_nombre','contacto_celular',
                        'contacto_correo' ),('zona','departamento','municipio'),
                        'gps','organizacion_civil',)
        }),
        )
    inlines = [RubrosPrincipalesInlines,ActividadEmpresarialInlines,
               MercadosRubrosInlines,CertificacionesRubrosInlines,
               FotosActividadEmpresarialInlines,MejoraEmpresaInline]
    list_display = ['nombre', 'tipo','zona','departamento']
    list_filter = ['nombre', 'zona']
    search_fields = ['nombre']

admin.site.register(Empresas, EmpresasAdmin)
admin.site.register(TipoEmpresa)
admin.site.register(Rubros)
admin.site.register(RubrosPrincipales)
admin.site.register(ActividadesEmpresariales)
admin.site.register(Mercados)
admin.site.register(MercadosCompradores)
admin.site.register(Certificaciones)
admin.site.register(ActividadEmpresarial)
admin.site.register(MercadosRubros)
#admin.site.register(CompradoresRubros)
admin.site.register(CertificacionesRubros)
admin.site.register(FotosActividadEmpresarial)
#-------------- admin de mejora empresarial -----------------------
class FotosMejoraEmpresaInline(admin.TabularInline):
    model = FotosMejoraEmpresa
    extra = 1

class DiasCampoEmpresaInline(admin.TabularInline):
    model = DiasCampoEmpresa
    extra = 1
    
class MejoraEmpresarialAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('nombre_mejora', 'empresa', 'fecha_prueba'), 
                       ('tema_prueba','rubro_prueba','mercado_prueba'),
                       ('fecha_inicio','fecha_finalizacion'),)
        }),
        ('La logica', {
            'fields': ('problema', 'causa','mejorar',
                        'resultados',)
        }),
        ('Resultados', {
            'fields': ('volumen_acopio', 'mejora_proce_calidad', 
                       'presentacion_acceso','inversion_credito',
                       'mejora_precio','mejora_ingreso','reduccion_costo',)
        }),
        
    )
    inlines = [FotosMejoraEmpresaInline,DiasCampoEmpresaInline]
    list_display = ['nombre_mejora','empresa','fecha_prueba', 'tema_prueba','color_completo']
    search_fields = ['empresa__nombre', 'nombre_mejora']
    list_filter = ['empresa__nombre', 'tema_prueba', 'rubro_prueba']

admin.site.register(MejoraEmpresas, MejoraEmpresarialAdmin)
admin.site.register(TemasEmpresa)
admin.site.register(DiasCampoEmpresa)
admin.site.register(FotosMejoraEmpresa)