# -*- coding: utf-8 -*-
from django import forms
from aristos.models import *
from aristos import ZeroPushHelper


class CircularForm(forms.ModelForm):
    class Meta:
        model = Circular
        fields = '__all__'

    enviarNotificacion = forms.BooleanField(label="Notificar Usuarios", initial=True, required=False)

    def save(self, commit=True):
        notification = self.cleaned_data.get('enviarNotificacion', None)
        if notification:
            instance = super(CircularForm, self).save(commit=True)
            ZeroPushHelper.send_broadcast_notification('Nueva Circular', instance.titulo, instance.id, 'circular')
        return super(CircularForm, self).save(commit=commit)


class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = '__all__'

    enviarNotificacion = forms.BooleanField(label="Notificar Usuarios", initial=True, required=False)

    def save(self, commit=True):
        notification = self.cleaned_data.get('enviarNotificacion', None)
        if notification:
            instance = super(AvisoForm, self).save(commit=True)
            print 'Send Notification'
            ZeroPushHelper.send_broadcast_notification('Nuevo Aviso', instance.titulo, instance.id, 'aviso')
        return super(AvisoForm, self).save(commit=commit)


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

    enviarNotificacion = forms.BooleanField(label="Notificar Usuarios", initial=True, required=False)

    def save(self, commit=True):
        notification = self.cleaned_data.get('enviarNotificacion', None)
        if notification:
            instance = super(EventoForm, self).save(commit=True)
            print 'Send Notification'
            ZeroPushHelper.send_broadcast_notification('Nuevo Evento', instance.titulo, instance.id, 'evento')
        return super(EventoForm, self).save(commit=commit)
