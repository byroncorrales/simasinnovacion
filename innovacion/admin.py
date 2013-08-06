from django.contrib import admin
from .models import *

class IniciativaInnovacionInline(admin.TabularInline):
	model = IniciativaInnovacion
	fields = ('fecha','nombre','tipo','fecha_inicio','fecha_finalizacion')
	extra = 1

class FotosInnovacionInline(admin.TabularInline):
	model = FotosInnovacion
	extra = 1

class EspacioInnovacionAdmin(admin.ModelAdmin):
	inlines = [IniciativaInnovacionInline]

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
admin.site.register(IniciativaInnovacion)
admin.site.register(FotosIniciativa)