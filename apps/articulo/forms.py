from django import forms
from apps.articulo.models import Articulo

class articuloForm(forms.ModelForm):
    class Meta:
        model= Articulo

        fields=[
            'titulo',
            'contenido',
            'imagen',
            'fecha_publicacion',
            'fecha_vencimiento',
            'tag',

        ]

        labels={
            'titulo':'Titulo',
            'contenido':'Contenido',
            'imagen':'Imagen',
            'fecha_publicacion': 'Fecha de Publicacion',
            'fecha_vencimiento': 'Fecha de vencimiento',
            'tag':'Tag',
        }

        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(),
            'fecha_publicacion': forms.SelectDateWidget(),
            'fecha_vencimiento':forms.SelectDateWidget(),
            'Tag':forms.CheckboxSelectMultiple(),
        }