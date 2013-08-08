from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('promotores.views',
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^lista/promotor/$', 'promotor_index', name="lista_promotor"),
    url(r'^promotor/(?P<id>\w+)/$', 'promotor_pagina', name="promotor_pagina"),
    url(r'^ver_mapa_completo/$', 'mapa_completo', name="mapa-completo"),
    
    # url(r'^(?P<slug>[-_\w]+)/$', view=EventosDetailView.as_view(), 
    #                              name='eventos_detalle'),
    )