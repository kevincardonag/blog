from django.db import models

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField()
    fecha_publicacion=models.DateField()
    fecha_vencimiento=models.DateField()
    def __str__(self):
        return "{}".format(self.titulo)
class Comentario(models.Model):
    articulo=models.ForeignKey(Articulo,blank=True,null=True,on_delete=models.CASCADE)
    comentario=models.TextField()
    def __str__(self):
        return "{}".format(self.comentario)

class Tag(models.Model):
    nombre=models.CharField(max_length=50)
    articulo=models.ManyToManyField(Articulo)
    def __str__(self):
        return "{}".format(self.nombre)