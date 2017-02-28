from django import forms

from datetimewidget.widgets import DateWidget
from articulo.models import Articulo, Comentario


class ArticuloForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticuloForm, self).__init__(*args, **kwargs)
        self.fields['fecha_vencimiento'].widget = \
            DateWidget(attrs={'id': "fecha_vencimiento", 'name': 'fecha_vencimiento'},
                       usel10n=True, bootstrap_version=3)

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

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['comentario'].widget.attrs.update({'style': 'width:100%', 'rows': '5'})

    class Meta:
        model = Comentario

        fields = [
            'comentario',
        ]
