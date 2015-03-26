# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Area(models.Model):
    nombreArea = models.CharField(max_length=200)

    def __str__(self):
        return self.nombreArea


class Usuario(models.Model):
    user = models.OneToOneField(User)
    area = models.ForeignKey(Area, blank=True, null=True)

    def __str__(self):
        return self.area.nombreArea


class Circular(models.Model):
    titulo = models.CharField(max_length=200, help_text='Título de la circular', verbose_name='Título')
    fechaPublicacion = models.DateField(verbose_name='Fecha de Publicación')
    contenido = models.CharField(max_length=200)
    remitente = models.ForeignKey(Usuario)

    class Meta:
        verbose_name_plural = "Circulares"

    def __str__(self):
        return self.titulo


class Aviso(models.Model):
    titulo = models.CharField(max_length=200, help_text='Titulo de el aviso', verbose_name='Título')
    fechaPublicacion = models.DateField(verbose_name='Fecha de Publicación')
    contenido = models.CharField(max_length=200)
    remitente = models.ForeignKey(Usuario)

    def __str__(self):
        return self.titulo


class Evento(models.Model):
    titulo = models.CharField(max_length=200, help_text='Titulo de el evento', verbose_name='Título')
    fechaInicio = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Inicio (HH:MM)', help_text='Fecha de Inicio del Evento')
    fechaFin = models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Fin (HH:MM)', help_text='Fecha de Fin del Evento')
    contenido = models.CharField(max_length=200)
    remitente = models.ForeignKey(Usuario)

    def __str__(self):
        return self.titulo








