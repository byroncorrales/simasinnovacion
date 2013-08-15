from django.conf.urls import patterns, url

urlpatterns = patterns('fortalecimiento.views',
        url(r'^$', 'fortalecimiento_index', name="lista_fortalecimiento"),
        url(r'^medio/(?P<id>\w+)/$', 'medios_pagina', name="medios_pagina"),
    	#url(r'^ficha/(?P<id>\w+)/$', 'mejora_pagina', name="mejora_pagina"),
    )