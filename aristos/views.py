from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse
from aristos.models import *
# Create your views here.


def circulares(request):
    data = serializers.serialize('json',Circular.objects.all())
    return HttpResponse(data, content_type='application/json')


def avisos(request):
    data = serializers.serialize('json',Aviso.objects.all())
    return HttpResponse(data, content_type='application/json')


def eventos(request):
    data = serializers.serialize('json',Evento.objects.all())
    return HttpResponse(data, content_type='application/json')