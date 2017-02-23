from django import forms
from .models  import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan

        fields = ['name', 'sumary', 'organizer',]

        labels = {
        	'name' : 'Nombre', 
        	'sumary' : 'Descripcion', 
        	'organizer' : 'Organizador',
        }

        widgets = {
        	'name' : forms.TextInput(attrs={'class': 'form-control'}), 
        	'sumary' : forms.Textarea(attrs={'class': 'form-control', 'rows': '2' }), 
        	'organizer' : forms.Select(attrs={'class': 'form-control'}),
        }