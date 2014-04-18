from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
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
    url(r'^segunda/$', TemplateView.as_view(template_name="seleccion.html")),
    url(r'^tercera/$', TemplateView.as_view(template_name="promotores.html")),
    url(r'^cuarta/$', TemplateView.as_view(template_name="fpromotor.html")),
    url(r'^quinta/$',TemplateView.as_view(template_name="fprueba.html")),
    url(r'^prueba/$',TemplateView.as_view(template_name="prueba.html")),
)

urlpatterns += staticfiles_urlpatterns()

if DEBUG:
    urlpatterns += patterns('',
                (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
                )