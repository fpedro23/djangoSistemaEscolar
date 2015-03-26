from django import forms
from aristos.models import *
from aristos import ZeroPushHelper


class CircularForm(forms.ModelForm):
    class Meta:
        model = Circular
        fields = '__all__'

    enviarNotificacion = forms.BooleanField(label="Notificar Usuarios", initial=True)

    def save(self, commit=True):
        notification = self.cleaned_data.get('enviarNotificacion', None)
        if notification:
            instance = super(CircularForm, self).save(commit=True)
            ZeroPushHelper.sendBroadcastNotification('Nueva Circular', instance.titulo, instance.id, 'circular')
        return super(CircularForm, self).save(commit=commit)


class AvisoForm(forms.ModelForm):
    class Meta:
        model = Aviso
        fields = '__all__'

    enviarNotificacion = forms.BooleanField(label="Notificar Usuarios", initial=True)

    def save(self, commit=True):
        notification = self.cleaned_data.get('enviarNotificacion', None)
        if notification:
            instance = super(AvisoForm, self).save(commit=False)
            print 'Send Notification'
            print instance.titulo
        return super(AvisoForm, self).save(commit=commit)


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

    enviarNotificacion = forms.BooleanField(label="Notificar Usuarios", initial=True)

    def save(self, commit=True):
        notification = self.cleaned_data.get('enviarNotificacion', None)
        if notification:
            instance = super(EventoForm, self).save(commit=False)
            print 'Send Notification'
            print instance.titulo
        return super(EventoForm, self).save(commit=commit)
