from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from settings import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('promotores.urls')),
    url(r'^', include('empresas.urls')),
    url(r'^fortalecimiento/', include('fortalecimiento.urls')),
    url(r'^servicios/', include('servicios.urls')),
    url(r'^', include('politicas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )