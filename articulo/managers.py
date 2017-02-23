from django.db import models
from django.db.models import Count, F


class TagManager(models.Manager):
    """
    Autor: Milton Lenis
    Fecha: Febrero 23 2017
    Manager personalizado para el modelo Tag
    """

    def obtener_cantidad_articulos_por_categoria(self):
        """
        Autor: Milton Lenis
        Fecha: Febrero 23 2017
        Método para obtener la cantidad de articulos por categoría, retorna un diccionario con la forma
        {"categoria":"cantidad"}
        :return: Diccionario con los datos
        """
        return self.annotate(cantidad_articulos=Count('articulo')).values('nombre', 'cantidad_articulos', 'id')

