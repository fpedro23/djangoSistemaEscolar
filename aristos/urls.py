from django.conf.urls import patterns, include, url
from django.contrib import admin
from aristos import views



urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^circulares/', views.circulares),
    url(r'^avisos/', views.avisos),
    url(r'^eventos/', views.eventos),

    # ex: /aristos/circular/5/
    url(r'^circular/(?P<id_element>\d+)/$', views.detallecircular),
    # ex: /aristos/aviso/5/
    url(r'^aviso/(?P<id_element>\d+)/$', views.detalleaviso),
    # ex: /aristos/evento/5/
    url(r'^evento/(?P<id_element>\d+)/$', views.detalleevento),



)
