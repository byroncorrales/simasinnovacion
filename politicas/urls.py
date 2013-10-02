from django.conf.urls import patterns, url


urlpatterns = patterns('politicas.views',

    url(r'^espacios/$', 'espacio_index', name="lista_espacios"),
    url(r'^espacio/(?P<id>\w+)/$', 'espacio_pagina', name="espacio_pagina"),
    #practicas
    #url(r'^practicas/$', 'practicas_index', name="lista_practicas"),
    url(r'^iniciativa/(?P<id>\w+)/$', 'iniciativa_pagina', name="practica_pagina"),
    url(r'^mapa_completo_espacios/$', 'mapa_completo_espacios', name="mapa-completo-espacios"),
    url(r'^iniciativa/$', 'iniciativa_index', name="lista-iniciativa"),
    )