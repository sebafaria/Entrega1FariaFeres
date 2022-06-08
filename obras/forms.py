from django import forms
from obras.models import Obra

class Obra_form(forms.Form):
    class Meta:
        model = Obra
        fields = '__all__'
