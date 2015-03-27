# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from aristos.forms import *


class UsuarioInLine(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Usuarios'


class UserAdmin(UserAdmin):
    inlines = (UsuarioInLine,)


class CircularAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'remitente', 'fechaPublicacion')
    form = CircularForm


class AvisoAdmin(admin.ModelAdmin):
    form = AvisoForm


class EventoAdmin(admin.ModelAdmin):
    form = EventoForm

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Circular, CircularAdmin)
admin.site.register(Aviso, AvisoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Area)