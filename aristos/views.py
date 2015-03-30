from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from aristos.models import *
from oauth2_provider.views.generic import ProtectedResourceView


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


def token(request):
    print request.GET
    return HttpResponse('hello', content_type='text')


# New implementation for the mobile API
# There is now a ProtectedResourceView subclass
# for every Entity, the get metho responds to both
# getAll and getById, depending on whether or not
# it receives an id paramter through the request
#
#
# Since each of these endpoints extendsProtectedResourceView
# we will get a 403 (unauthorized) response unless
# you provide a valid access token through the get request
# other than that, it works just as the previous implementation
class CircularEndpoint(ProtectedResourceView):

    def get(self, request, *args, **kwargs):
        if request.GET.get('id', False):
            data = serializers.serialize('json', Circular.objects.filter(id=request.GET.get('id')), use_natural_keys=True)
        else:
            data = serializers.serialize('json', Circular.objects.all(), use_natural_keys=True,)
        return HttpResponse(data, content_type='application/json')


class AvisoEndpoint(ProtectedResourceView):

    def get(self, request, *Args, **kwargs):
        if(request.GET.get('id', False)):
            data = serializers.serialize('json', Aviso.objects.filter(id=request.GET['id']), use_natural_keys=True)
        else:
            data = serializers.serialize('json', Aviso.objects.all(), use_natural_keys=True)
        return HttpResponse(data, 'application/json')


class EventoEndpint(ProtectedResourceView):

    def get(self, request, *args, **kwargs):
        if(request.GET.get('id', False)):
            data = serializers.serialize('json', Evento.objects.filter(id=request.GET['id']), use_natural_keys=True)
        else:
            data = serializers.serialize('json', Evento.objects.all(), use_natural_keys=True)
        return HttpResponse(data, 'application/json')