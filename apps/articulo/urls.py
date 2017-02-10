from django.conf.urls import url,include
from apps.articulo.views import index,crearArticulo

urlpatterns = [
    url(r'^$',crearArticulo,name='index'),
]