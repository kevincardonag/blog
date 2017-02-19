from django.conf.urls import url,include

from apps.articulo.views import index,listarArticulos,mostrarArticulo,editarArticulo,crearComentario

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^listar/(?P<id_tag>\d+)/$',listarArticulos,name='listar'),
    url(r'^listarArticulo/(?P<pk>\d+)/$',mostrarArticulo.as_view(),name='mostrar'),
    url(r'^editarArticulo/(?P<id_articulo>\d+)/$', editarArticulo, name='editar'),
    url(r'^crearArticulo/(?P<pk>\d+)/$',crearComentario.as_view(),name='crearComentario'),
]