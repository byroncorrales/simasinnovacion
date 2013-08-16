from django.conf.urls import patterns, url

urlpatterns = patterns('servicios.views',
        url(r'^$', 'servicios_index', name="lista_servicios"),
        url(r'^servicio/(?P<id>\w+)/$', 'servicios_pagina', name="servicios_pagina"),
        #url(r'^ficha/(?P<id>\w+)/$', 'mejora_pagina', name="mejora_pagina"),
    )