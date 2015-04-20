# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from aristos.forms import *
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist


class UsuarioInLine(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Usuarios'


class UserAdmin(UserAdmin):
    inlines = (UsuarioInLine,)


class CircularAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'remitente', 'fechaPublicacion')
    form = CircularForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "remitente":
            try:
                kwargs["queryset"] = Area.objects.filter(Q(id=request.user.usuario.area.id))
            except ObjectDoesNotExist:
                kwargs["queryset"] = Area.objects.all()

        return super(
            CircularAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class AvisoAdmin(admin.ModelAdmin):
    form = AvisoForm
    list_display = ('titulo', 'remitente', 'fechaPublicacion')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "remitente":
            try:
                kwargs["queryset"] = Area.objects.filter(Q(id=request.user.usuario.area.id))
            except ObjectDoesNotExist:
                kwargs["queryset"] = Area.objects.all()

        return super(
            AvisoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class EventoAdmin(admin.ModelAdmin):
    form = EventoForm
    list_display = ('titulo', 'remitente', 'fechaInicio', 'fechaFin')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "remitente":
            try:
                kwargs["queryset"] = Area.objects.filter(Q(id=request.user.usuario.area.id))
            except ObjectDoesNotExist:
                kwargs["queryset"] = Area.objects.all()

        return super(
            EventoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Circular, CircularAdmin)
admin.site.register(Aviso, AvisoAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Area)