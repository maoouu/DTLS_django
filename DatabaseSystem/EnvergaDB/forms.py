from django import forms
from django.forms import fields, widgets
from .models import Records


class RecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['author', 'file_desc', 'action_desc', 'status']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'file_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'action_desc': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
