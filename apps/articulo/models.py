from django.db import models

# Create your models here.

class Tag(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return "{}".format(self.nombre)
class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='media/pictures',blank=True,null=True)
    fecha_publicacion=models.DateField(null=True,blank=True)
    fecha_vencimiento=models.DateField(null=True,blank=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return "{}".format(self.titulo)
class Comentario(models.Model):
    articulo=models.ForeignKey(Articulo,blank=True,null=True,on_delete=models.CASCADE)
    comentario=models.TextField()
    def __str__(self):
        return "{}".format(self.comentario)

