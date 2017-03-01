from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from django.views.generic import CreateView
from usuario.forms import UserCreateForm


class UserCreateView(CreateView):
    """
    Autor: Kevin Cardona
    Fecha: 27 Febrero 2017
    clase create View para la creacion de usuarios
    """
    model = User
    template_name = 'usuario/crear.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('articulo:index')
