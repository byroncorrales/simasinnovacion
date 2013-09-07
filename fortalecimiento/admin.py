from django.contrib import admin
from .models import *

class ParticipantesInline(admin.TabularInline):
	model = Participantes
	extra = 1

class NivelConocimientoInline(admin.TabularInline):
	model = NivelConocimiento
	extra = 1

class FotosMediosInline(admin.TabularInline):
	model = FotosMedios
	extra = 1

class MediosFortalecimientoAdmin(admin.ModelAdmin):
	filter_horizontal = ['tipo_medio','temas','grupos_metas','papel_simas']
	inlines = [ParticipantesInline,NivelConocimientoInline,
				FotosMediosInline]
	list_display = ['nombre','get_medios','get_temas']
	list_filter = ['papel_simas','grupos_metas']
	search_fields = ['nombre'] 

admin.site.register(MediosFortalecimiento, MediosFortalecimientoAdmin)
admin.site.register(TiposMedios)
admin.site.register(TemasAbordan)
admin.site.register(GruposMetas)
admin.site.register(PapelSimas)
admin.site.register(PersonasResultados)
admin.site.register(Participantes)
admin.site.register(NivelConocimiento)
admin.site.register(FotosMedios)