from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

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

    def get_success_url(self):
        return reverse('articulo:index')

    def form_valid(self, form):
        """
        Autor: Kevin Cardona
        Fecha: 4 marzo 2017
        metodo form_valid que autentica el usuario, luego de su creacion.
        :param form:
        :return:
        """
        super(UserCreateView, self).form_valid(form)
        user = authenticate(username=self.object.username, password=self.request.POST.get('password1'))
        if user is not None:
            login(self.request, user)
        return redirect(reverse('articulo:index'))
