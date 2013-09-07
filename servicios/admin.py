from django.contrib import admin
from .models import *

class ResultadoEvaluacionInline(admin.TabularInline):
    model = ResultadoEvaluacion
    extra = 1

class FotosServiciosInline(admin.TabularInline):
    model = FotosServicios
    extra = 1

class ServiciosAdmin(admin.ModelAdmin):
    filter_horizontal = ['benefician_servicio','tipos_servicios','temas_abordan','org_benefician']
    inlines = [ResultadoEvaluacionInline,FotosServiciosInline]
    list_display = ['nombre','solicita_servicio','fecha_inicio','fecha_finalizacion']
    list_filter = ['tipos_servicios','temas_abordan']
    search_fields = ['nombre']

admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(OrganizacionSolicita)
admin.site.register(OrganizacionBenefician)
admin.site.register(TiposServicio)
admin.site.register(TemasAbordan)
admin.site.register(TiposOrganizacionBenefician)
admin.site.register(EvaluacionServicio)
admin.site.register(ResultadoEvaluacion)
admin.site.register(FotosServicios)