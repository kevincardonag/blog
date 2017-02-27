from django.db import models
from django.db.models import Count


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
        return self.annotate(cantidad_articulos=models.Sum(
            models.Case(models.When(articulo__estado=True, then=1),
                        default=0, output_field=models.IntegerField()
                        )
            )
        )


class ArticuloManager(models.Manager):
    """
    Autor: Kevin Cardona
    Fecha: 27 febrero 2017
    Manager personalizado para el modelo Tag
    """

    def buscar_articulos_por_categoria_y_estado(self, id_tag, estado):
        """
        Autor: Kevin Cardona
        Fecha: 27 febrero 2017
        Metodo para obtener todos los articulos correspondiente a una categoria y con un estado (True or False)
        :param id_tag
        :return: lista con articulos
        """
        return self.filter(tag__id=id_tag, estado=estado)

    def buscar_articulos_por_estado(self, estado):
        """
        Autor: Kevin Cardona
        Fecha: 27 Febrero 2017
        Metodo que obtiene todos los articulos por un estado, (True or False)
        :param estado:
        :return: lista con articulos
        """

        return self.filter(estado=estado)
