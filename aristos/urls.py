from django.conf.urls import patterns, include, url
from django.contrib import admin
from aristos import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoSistemaEscolar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^circulares/', views.circulares),
    url(r'^avisos/', views.avisos),
    url(r'^eventos/', views.eventos),
)
