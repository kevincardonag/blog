from django.conf.urls import url,include

from articulo import views

urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^crear-articulo/$', views.Crear_articulo.as_view(), name='crearArticulo'),
    url(r'^listar/(?P<id_tag>\d+)/$', views.Listar_articulos.as_view(), name='listar'),
    url(r'^listarArticulo/(?P<pk>\d+)/$', views.mostrarArticulo.as_view(), name='mostrar'),
    url(r'^editarArticulo/(?P<id_articulo>\d+)/$', views.editarArticulo, name='editar'),
    url(r'^crearArticulo/(?P<pk>\d+)/$', views.crearComentario.as_view(), name='crearComentario'),
]

