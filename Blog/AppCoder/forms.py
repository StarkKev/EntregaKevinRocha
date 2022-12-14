from django import forms

class VideojuegosFormulario(forms.Form):
    videojuegos = forms.CharField()
    genero=forms.CharField()
    ano_lanzamiento=forms.IntegerField()

class PlataformasFormulario(forms.Form):
    plataformas = forms.CharField()
    precio=forms.CharField()
    ano_lanzamiento=forms.IntegerField()

class HardwareFormulario(forms.Form):
    hardware = forms.CharField()
    distribuidor=forms.CharField()
    precio=forms.IntegerField()