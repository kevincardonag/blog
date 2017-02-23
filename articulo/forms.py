from django import forms
from articulo.models import Articulo,Comentario

class articuloForm(forms.ModelForm):
    class Meta:
        model= Articulo

        fields=[
            'titulo',
            'contenido',
            'imagen',
            'fecha_vencimiento',
            'tag',

        ]

        labels={
            'titulo':'Titulo',
            'contenido':'Contenido',
            'imagen':'Imagen',
            'fecha_vencimiento': 'Fecha de vencimiento',
            'tag':'Tag',
        }

        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control','required':True}),
            'contenido':forms.Textarea(attrs={'class':'form-control','required':True}),
            'imagen':forms.FileInput(),
            'fecha_vencimiento':forms.SelectDateWidget(attrs={'class':'text-dark','required':True}),
            'Tag':forms.CheckboxSelectMultiple(attrs={'class':'text-dark'}),
        }

class comentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario

        fields=[
            'comentario',
        ]

        labels={
            'comentario':'comentario',
        }

        widgets={
            'comentario':forms.Textarea(attrs={'class':'form-class','rows':'4','style':'width:100%','required':'True'}),
        }