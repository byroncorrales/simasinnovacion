from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('promotores.views',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^inicio/$', 'inicio', name="inicio"),
    url(r'^promotores/$', 'promotor_index', name="lista_promotor"),
    url(r'^promotor/(?P<id>\w+)/$', 'promotor_pagina', name="promotor_pagina"),
    url(r'^ver_mapa_completo_index/$', 'mapa_completo_index', name="mapa-completo-index"),
    url(r'^ver_mapa_completo/$', 'mapa_completo', name="mapa-completo"),
    #practicas
    url(r'^practicas/$', 'practicas_index', name="lista_practicas"),
    url(r'^practica/(?P<id>\w+)/$', 'practica_pagina', name="practica_pagina"),
    url(r'^mapa_completo_practica/$', 'mapa_completo_practica', name="mapa-completo-practica"),
    #KronosCode Cambios
    url(r'^gpromotor/$', 'gpromotor', name="gpromotor"),
    )