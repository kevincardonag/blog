from django.conf.urls import url,include
from apps.articulo.views import index,listarArticulos,mostrarArticulo

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^listar/(?P<id_tag>\d+)/$',listarArticulos,name='listar'),
    url(r'^listarArticulo/(?P<id_articulo>\d+)/$',mostrarArticulo,name='mostrar'),
]