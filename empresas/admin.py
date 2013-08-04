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
			   MercadosRubrosInlines,CompradoresRubrosInlines,
			   CertificacionesRubrosInlines,FotosActividadEmpresarialInlines]

admin.site.register(Empresas, EmpresasAdmin)
admin.site.register(TipoEmpresa)
admin.site.register(Rubros)
admin.site.register(RubrosPrincipales)
admin.site.register(ActividadesEmpresariales)
admin.site.register(Mercados)
admin.site.register(Certificaciones)
admin.site.register(ActividadEmpresarial)
admin.site.register(MercadosRubros)
admin.site.register(CompradoresRubros)
admin.site.register(CertificacionesRubros)
admin.site.register(FotosActividadEmpresarial)

