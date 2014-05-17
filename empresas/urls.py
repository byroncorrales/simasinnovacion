from django.conf.urls import patterns, url

urlpatterns = patterns('empresas.views',
        url(r'^empresas/$', 'empresas_index', name="lista_empresas"),
        url(r'^empresa/(?P<id>\w+)/$', 'empresas_pagina', name="empresas_pagina"),
        url(r'^mapa_completo_empresa/$', 'mapa_completo_empresa', name="mapa-completo-index"),
    	
        url(r'^mejoras/$', 'mejoras_index', name="mejora_index"),
        url(r'^mejora/(?P<id>\w+)/$', 'mejora_pagina', name="mejora_pagina"),
        #Cambios Kronos Code
        url(r'^empresa/$', 'empresa', name="listar_empresas"),
        url(r'^fempresa/(?P<id>\w+)/$', 'fempresa', name="ficha_empresa"),
        url(r'^fmejora/(?P<id>\w+)/$', 'fmejora', name="ficha_mejora"),
        url(r'^mejora/$', 'mejora', name="listar_mejora")
    )