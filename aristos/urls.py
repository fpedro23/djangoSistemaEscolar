from django.conf.urls import patterns, url
from aristos import views

urlpatterns = patterns('',
    # Mappings for the new (protected) implementation of the mobile API
    url(r'^api/circular', views.CircularEndpoint.as_view()),
    url(r'^api/aviso', views.AvisoEndpoint.as_view()),
    url(r'^api/evento', views.EventoEndpint.as_view()),

)
