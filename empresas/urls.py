from django.conf.urls import patterns, url

urlpatterns = patterns('empresas.views',
        url(r'^$', 'empresas_index', name="lista_empresas"),
        url(r'^empresa/(?P<id>\w+)/$', 'empresas_pagina', name="empresas_pagina"),
        url(r'^mapa_completo_empresa/$', 'mapa_completo_empresa', name="mapa-completo-index"),
    	
        url(r'^mejoras/$', 'mejoras_index', name="mejora_index"),
        url(r'^mejora/(?P<id>\w+)/$', 'mejora_pagina', name="mejora_pagina"),
    )