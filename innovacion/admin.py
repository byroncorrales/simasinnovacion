#encoding: utf-8
#
from django.contrib import admin
from .models import *

class IniciativaInnovacionInline(admin.TabularInline):
	model = IniciativaInnovacion
	fields = ('fecha','nombre','tipo','fecha_inicio','fecha_finalizacion')
	extra = 1

class FotosInnovacionInline(admin.TabularInline):
	model = FotosInnovacion
	extra = 1

class ActividadEmpresarialInline(admin.TabularInline):
	model = ActividadEmpresarial
	extra = 1

class EspacioInnovacionAdmin(admin.ModelAdmin):
	filter_horizontal = ('departamento_influye','municipios_influye',
                        'papel','temas')
	fieldsets = (
		(None, {
			'fields': (('nombre', 'tipos', 'activos','tiempo_formado'),
                        ('nombre_contacto','celular_contacto',
                        'correo_contacto' ),('zona','cobertura'),'departamento_influye',
                        'municipios_influye','numero_entidades','papel','temas',)
		}),
		)
	inlines = [ActividadEmpresarialInline,FotosInnovacionInline,
				IniciativaInnovacionInline]
	list_display = ['nombre','tipos','zona','cobertura']
	list_filter = ['departamento_influye','papel']
	search_fields = ['nombre']

admin.site.register(EspacioInnovacion, EspacioInnovacionAdmin)
admin.site.register(TipoEspacio)
admin.site.register(PapelSimas)
admin.site.register(TemasIncidencia)
admin.site.register(ActividadesEspacio)
admin.site.register(ActividadEmpresarial)
admin.site.register(FotosInnovacion)
admin.site.register(TipoIniciativa)
admin.site.register(TemasAborda)
admin.site.register(ActividadIniciativa)

class FotosInicitivasInline(admin.TabularInline):
	model = FotosIniciativa
	extra = 1

class IniciativaInnovacionAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (('fecha', 'nombre', 'espacio'),
                        ('tipo','fecha_inicio','fecha_finalizacion' ),
                        'temas','actividades',)
		}),
		('La lógica de la iniciativa', {
			'fields': ('problema', 'analisis', 'enfoque',
                       'resultado',)
		}),
		('Resultados obtenidos de la iniciativa', {
			'fields': ('sobre_tierra', 'fomento', 'conservacion',
                       'inversion','acceso_mercado','comunicacion',
                       'reduccion')
		}),
		)
	inlines = [FotosInicitivasInline]
	list_display = ['nombre','fecha','espacio','color_completo']
	list_filter = ['tipo','temas']
	search_fields = ['nombre']

admin.site.register(IniciativaInnovacion, IniciativaInnovacionAdmin)
admin.site.register(FotosIniciativa)