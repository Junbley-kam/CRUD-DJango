from django import forms
from .models import Doctor

class TaskForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad', 'horarios_del_profesional', 'consultorio']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'horarios_del_profesional': forms.TextInput(attrs={'class': 'form-control'}),
            'consultorio': forms.TextInput(attrs={'class': 'form-control'}),
        }