from django import forms
from obras.models import Obra

class Obra_form(forms.Modelform):
    class Meta:
        model = Obra
        fields = '__all__'
