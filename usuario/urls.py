from django.conf.urls import url
from django.contrib.auth.views import login, logout
from usuario.views import UserCreateView

urlpatterns = [
    url(r'^registrar$', UserCreateView.as_view(), name='registrar'),
    url(r'^inciar-sesion$', login, {'template_name': 'usuario/iniciar-sesion.html'}, name='iniciar-sesion'),
    url(r'^logout$', logout, {'next_page': 'articulo:index'}, name='logout'),
]
