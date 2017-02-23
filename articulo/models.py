from django.db import models
from .managers import TagManager
import datetime


class Tag(models.Model):
    nombre = models.CharField(max_length=50)
    objects = models.Manager()
    custom_objects = TagManager()

    def __str__(self):
        return "{}".format(self.nombre)


class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='pictures',blank=True,null=True)
    fecha_publicacion=models.DateField(auto_now_add=True)
    fecha_vencimiento=models.DateField(null=True,blank=True)
    estado=models.BooleanField(default=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return "{}".format(self.titulo)


class Comentario(models.Model):
    articulo=models.ForeignKey(Articulo,blank=True,null=True,on_delete=models.CASCADE)
    comentario=models.TextField()

    def __str__(self):
        return "{}".format(self.comentario)

