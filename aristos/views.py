from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls import patterns
from django.core import serializers
from aristos.models import *
from django.contrib import admin


# Create your views here.
def circulares(request):
    data = serializers.serialize('json',
                                 Circular.objects.all(),
                                 use_natural_keys=True,
    )
    return HttpResponse(data, content_type='application/json')


def avisos(request):
    data = serializers.serialize('json',
                                 Aviso.objects.all(),
                                 use_natural_keys=True,
    )
    return HttpResponse(data, content_type='application/json')


def eventos(request):
    data = serializers.serialize('json', Evento.objects.all(), use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')


def detallecircular(request, id_element):
    data = serializers.serialize('json', Circular.objects.filter(id=id_element), use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')


def detalleaviso(request, id_element):
    data = serializers.serialize('json', Aviso.objects.filter(id=id_element), use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')


def detalleevento(request, id_element):
    data = serializers.serialize('json', Evento.objects.filter(id=id_element), use_natural_keys=True)
    return HttpResponse(data, content_type='application/json')


def admin(request):
    return HttpResponseRedirect('templates/admin/base.html')


def get_admin_urls(urls):
    def get_urls():
        my_urls = patterns('',
            (r'^tempaltes/$', admin.site.admin_view('templates'))
        )
        return my_urls + urls
    return get_urls


def token(request):
    print request.GET
    return HttpResponse('hello', content_type='text')
