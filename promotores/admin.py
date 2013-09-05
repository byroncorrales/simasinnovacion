from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin

class FotosPromotorInline(AdminImageMixin, admin.TabularInline):
    model = FotosPromotor
    extra = 1

class FotosPracticasInline(admin.TabularInline):
    model = FotosPrueba
    extra = 1

class DiasCampoPruebaInline(admin.TabularInline):
    model = DiasCampoPrueba
    extra = 1

class PruebaInline(admin.TabularInline):
    model = PracticasProductivas
    fields = ('fecha_prueba','nombre_prueba','tema_prueba',
              'rubro_prueba', 'escala_prueba')
    extra = 1

class PromotorAdmin(admin.ModelAdmin):
    list_display= ['nombre','sexo','edad','finca']
    search_fields = ('nombre',)
    list_filter = ['zona','escuela',]
    filter_horizontal = ('cultivos_finca','animales_finca',
                        'producto_procesado','mercado_accede')
    fieldsets = (
        (None, {
            'fields': (('nombre', 'sexo', 'edad'), ('educacion','contacto','activo'),
                      ('zona', 'departamento', 'municipio'),'gps',('organizacion_campesina',
                      'organizacion_civil','escuela','tipo_suelo','tipo_clima'),
                      ('meses_lluvia','finca','riego'),)
        }),
        ('Uso de tierra', {
            'fields': (('bosque', 'potrero'),('tacotales','forestal'),('perennes','lena'),
                        ('anuales','frutales'),('potrero_abierto','patio'),)
        }),
        (None, {
            'fields': (('cultivos_finca', 'animales_finca'), 
                        ('producto_procesado','mercado_accede'),)
        }),
        
    )
    inlines = [FotosPromotorInline,PruebaInline]

    class Media:
        css = {
            "all": ("css/my_custom_admin.css",)
        }

class PracticasProductivasAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': (('promotor', 'nombre_prueba', 'fecha_prueba'), 
                       ('tema_prueba','rubro_prueba','escala_prueba'),
                       'historia',('fecha_inicio','fecha_finalizacion'),)
        }),
        ('La logica', {
            'fields': ('problema', 'agroecologico','aprobar',
                        'resultados',)
        }),
        ('Resultados', {
            'fields': ('salud_planta', 'vida_suelo', 
                       'prod_rendimiento','calidad_producto',
                       'plagas','costo',)
        }),
        
    )
    inlines = [FotosPracticasInline,DiasCampoPruebaInline]
    list_display = ['nombre_prueba','promotor','fecha_prueba','tema_prueba','color_completo']
    list_filter = ['tema_prueba','rubro_prueba','escala_prueba']
    search_fields = ['nombre_prueba','promotor__nombre']

admin.site.register(Promotor, PromotorAdmin)
admin.site.register(OrganizacionCampesina)
admin.site.register(OrganizacionCivil)
admin.site.register(EscuelaCampo)
admin.site.register(CultivosFinca)
admin.site.register(AnimalesFinca)
admin.site.register(ProductoProcesado)
admin.site.register(MercadoAcceso)
admin.site.register(TipoSuelo)
#practicas
admin.site.register(PracticasProductivas, PracticasProductivasAdmin)
admin.site.register(TemasPruebas)
admin.site.register(RubroPruebas)
admin.site.register(EscalaPruebas)