from django.conf.urls import patterns, url, include
from aristos import views



urlpatterns = patterns('',
    url(r'^admin/', views.admin),
    url(r'^circulares/', views.circulares),
    url(r'^avisos/', views.avisos),
    url(r'^eventos/', views.eventos),
    url(r'^authorize_token/', views.token),

    # ex: /aristos/circular/5/
    url(r'^circular/(?P<id_element>\d+)/$', views.detallecircular),
    # ex: /aristos/aviso/5/
    url(r'^aviso/(?P<id_element>\d+)/$', views.detalleaviso),
    # ex: /aristos/evento/5/
    url(r'^evento/(?P<id_element>\d+)/$', views.detalleevento),



)
