from django.core.management import BaseCommand
from apps.articulo.models import Articulo,Comentario,Tag

class Command(BaseCommand):
    def __tags_create(self):
        historia = Tag(nombre='Historia')
        historia.save()
        ciencia = Tag(nombre='Ciencia')
        ciencia.save()
        Matematica = Tag(nombre='Matemáticas')
        Matematica.save()
        Filosofia=Tag(nombre='Filosofía')
        Filosofia.save()
    def handle(self, *args, **options):
        self.__tags_create()