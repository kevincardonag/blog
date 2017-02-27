from django.db import models
from .managers import TagManager, ArticuloManager


class Tag(models.Model):
    """
    Autor:Kevin Cardona
    Fecha:23 de febrero 2017
    clase del modelo tag
    """
    nombre = models.CharField(max_length=50)
    objects = models.Manager()
    custom_objects = TagManager()

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    """
    Autor:Kevin Cardona
    Fecha:23 de febrero 2017
    clase del modelo Articulo
    """
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='pictures', blank=True, null=True)
    fecha_publicacion = models.DateField(auto_now_add=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag)
    objects = models.Manager()
    custom_objects = ArticuloManager()

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    """
    Autor:Kevin Cardona
    Fecha:23 de febrero 2017
    clase del modelo Comentario
    """
    articulo = models.ForeignKey(Articulo, blank=True, null=True, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return self.comentario
