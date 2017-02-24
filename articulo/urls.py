from django.conf.urls import url

from articulo import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^crear-articulo/$', views.ArticuloCreateView.as_view(), name='crearArticulo'),
    url(r'^listar/(?P<id_tag>\d+)/$', views.ArticuloListView.as_view(), name='listar'),
    url(r'^listar-articulo/(?P<pk>\d+)/$', views.ArticuloDetailView.as_view(), name='mostrar'),
    url(r'^editar-articulo/(?P<pk>\d+)/$', views.ArticuloUpdateView.as_view(), name='editar'),
    url(r'^crear-articulo/(?P<pk>\d+)/$', views.ComentarioCreateView.as_view(), name='crearComentario'),
]
