from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from articulo import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^crear-articulo/$', login_required(views.ArticuloCreateView.as_view()), name='crear'),
    url(r'^listar/(?P<id_tag>\d+)/$', views.ArticuloListView.as_view(), name='listar'),
    url(r'^ver/(?P<pk>\d+)/$', views.ArticuloDetailView.as_view(), name='mostrar'),
    url(r'^editar-articulo/(?P<pk>\d+)/$', login_required(views.ArticuloUpdateView.as_view()), name='editar'),
    url(r'^crear-comentario/(?P<pk>\d+)/$', views.ComentarioCreateView.as_view(), name='crear-comentario'),
]
