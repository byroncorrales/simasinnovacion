from django.conf.urls import patterns, url


urlpatterns = patterns('innovacion.views',

    url(r'^espacios/$', 'espacio_index', name="lista_espacios"),
    url(r'^espacio/(?P<id>\w+)/$', 'espacio_pagina', name="espacio_pagina"),
    #url(r'^ver_mapa_completo_index/$', 'mapa_completo_index', name="mapa-completo-index"),
    #url(r'^ver_mapa_completo/$', 'mapa_completo', name="mapa-completo"),
    #practicas
    #url(r'^practicas/$', 'practicas_index', name="lista_practicas"),
    url(r'^iniciativa/(?P<id>\w+)/$', 'iniciativa_pagina', name="practica_pagina"),
    #url(r'^mapa_completo_practica/$', 'mapa_completo_practica', name="mapa-completo-practica"),
    )