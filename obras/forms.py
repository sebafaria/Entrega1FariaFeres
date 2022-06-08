from django import forms
from obras.models import Obra

#class Obra_form(forms.Form):
#    class Meta:
#        model = Obra
#        fields = '__all__'

class Obra_form(forms.Form):
    cliente = forms.CharField(max_length=100)
    nrocliente = forms.FloatField()
    nombre = forms.CharField(max_length=100)
    fecha = forms.DateField()
