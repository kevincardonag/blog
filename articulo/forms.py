from django import forms

from articulo.models import Articulo, Comentario


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo

        fields = [
            'titulo',
            'contenido',
            'imagen',
            'fecha_vencimiento',
            'tag',
        ]


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario

        fields = [
            'comentario',
        ]
