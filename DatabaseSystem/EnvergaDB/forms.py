from django import forms
from django.forms import fields, widgets
from .models import Records


class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['author', 'description', 'status']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'descripton': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
