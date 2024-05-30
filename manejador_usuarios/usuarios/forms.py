from django import forms
from .models import Usuario, Empleado

class UsuarioForm(forms.ModelForm):
    Id = forms.IntegerField(label='ID de Solicitud', required=True)
    class Meta:
        model = Usuario
        fields = [
            'nombre',
            'apellido',
            'tipo de identificacion',
            'numero de identificacion',
            'correo',
            'telefono', 
            'pais',
            'actividad economica',
            'ingresos',
            'deudas',
            'ciudad',
            'profesion',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'tipo de identificacion': 'Tipo de Identificacion',
            'numero de identificacion': 'Numero de Identificacion',
            'correo': 'Correo',
            'telefono': 'Telefono', 
            'pais': 'País',
            'actividad economica': 'Actividad Economica',
            'ingresos': 'Ingresos',
            'deudas': 'Deudas',
            'ciudad': 'Ciudad',
            'profesion': 'Profesión',
        }

class EmpleadoForm(forms.ModelForm):
    Id = forms.IntegerField(label='ID de Solicitud', required=True)
    class Meta:
        model = Empleado
        fields = [
            'nombre',
            'apellido',
            'identificacion',
            'cargo',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'identificacion': "Número de identificación",
            'cargo': 'Cargo',
        }