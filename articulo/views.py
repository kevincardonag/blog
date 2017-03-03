from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.contrib import messages

from django.views.generic import CreateView, ListView, DetailView, UpdateView
from articulo.models import Articulo, Tag, Comentario
from articulo.forms import ArticuloForm, ComentarioForm


class ArticuloCreateView(CreateView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase CreateView, para la creacion de articulos
    """
    model = Articulo
    template_name = 'articulo/crear-articulo.html'
    form_class = ArticuloForm

    def get_success_url(self):
        """
        Autor: Kevin Cardona
        Fecha: 4 marzo 2017
        despues de crear un articulo se envia un mensaje de confirmacion, y se redirecciona a la url correspondiente del
        artiuclo creado
        :return: redireccion al detalle de un articulo.
        """
        messages.success(self.request, "Artículo creado")
        return reverse('articulo:mostrar', kwargs={'pk': self.object.id})


class Index(ListView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase index, se lista todas las categorias(Tags) y cantidad de articulos por cada categoria
    """
    model = Tag
    template_name = 'articulo/index.html'
    
    def get_context_data(self, **kwargs):
        """
        Autor: Kevin Cardona
        Fecha: 4 marzo 2017
        se utiliza el manager del modelo Tag, para consultar cuantos articulos corresponden a cada categoria.
        :param kwargs:
        :return: retorna el context, como un diccionario.
        """
        context = super(Index, self).get_context_data(**kwargs)
        context['info_articulos'] = Tag.custom_objects.obtener_cantidad_articulos_por_categoria()
        return context


class ArticuloListView(ListView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase ListView, encargada de listar los articulos por una categoria
    """
    model = Articulo
    template_name = 'articulo/listar-articulos.html'

    def get_context_data(self, **kwargs):
        """
        Autor: Kevin Cardona
        Fecha: 4 marzo 2017
        se utiliza el manager del modelo Articulo, para consultar los articulos correspodientes a una categoria y con
        un estado True
        :param kwargs:
        :return: retorna el context, con los articulos de una categoria y estado True.
        """
        context = super(ArticuloListView, self).get_context_data(**kwargs)
        context['articulos'] = Articulo.custom_objects.buscar_articulos_por_categoria_y_estado(
                                                                    self.kwargs['id_tag'], True)
        return context


class ArticuloDetailView(DetailView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase DetailView, muestra un articulo en detalle
    """
    model = Articulo
    template_name = 'articulo/mostrar.html'

    def get_context_data(self, **kwargs):
        """
        Autor: Kevin Cardona
        Fecha: 4 Marzo 2017
        se envia por el contexto 3 parametros, todos los comentarios correspondientes a un articulo, el formulario
        instaciado de un articulo y el formulario para la creacion de articulos respectivamente.
        :param kwargs:
        :return:
        """
        context = super(ArticuloDetailView, self).get_context_data(**kwargs)
        articulo = self.get_object()
        context['comentarios'] = Comentario.objects.filter(articulo_id=articulo.pk)
        context['form2'] = ArticuloForm(instance=articulo)
        context['form_comentario'] = ComentarioForm()
        return context

    def get(self, request, *args, **kwargs):
        """
        Autor: Kevin Cardona Giraldo
        Fecha: 4 marzo 2017
        metodo encargado de verificar si hay una peticion ajax para el cambio de estado de un articulo.
        :param request:
        :param args:
        :param kwargs:
        :return: retorna el super del metodo, para la continuacion de los metodos de la clase.
        """
        if self.request.is_ajax():
            activado = self.request.GET.get('activado')
            articulo = self.get_object()
            if activado == '1':
                articulo.estado = False
                articulo.save()
                return HttpResponse('Estado: Desactivado')
            else:
                articulo.estado = True
                articulo.save()
                return HttpResponse('Estado: Desactivado')
        return super(ArticuloDetailView, self).get(request, *args, **kwargs)


class ArticuloUpdateView(UpdateView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase updateview,se encarga de actualizar un articulo
    """
    model = Articulo
    template_name = 'articulo/index.html'
    form_class = ArticuloForm

    def get_success_url(self, **kwargs):
        """
        Autor: Kevin Cardona
        Fecha: 4 marzo 2017
        metodo para redireccionar al articulo modificado, y envia un mensaje de exito
        :param kwargs:
        :return: retonar una redireccion a mostrar articulo
        """
        articulo = self.get_object()
        messages.success(self.request, 'Artículo modificado con éxito')
        return reverse('articulo:mostrar', kwargs={'pk': articulo.id})


class ComentarioCreateView(CreateView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase CreateView, para la creacion de comentarios
    """
    model = Comentario
    template_name = 'articulo/mostrar.html'
    form_class = ComentarioForm

    def get_success_url(self):
        """
        Autor: Kevin Cardona
        Fecha: 4 marzo 2017
        metodo para redireccionar luego de crear un comentario, se redirecciona al articulo donde fue creado el
        comentario
        :return: reverse al detalle de un articulo
        """
        id_articulo = self.kwargs['pk']
        return reverse('articulo:mostrar', kwargs={'pk': id_articulo})

    def form_valid(self, form):
        """
        Autor: Kevin Cardona
        Fecha: 4 marzo 2017
        metodo form_valid encargado de asignar un usuario y un articulo a un comentario.
        :param form:
        :return: retorna el super del metodo, para la continuacion de la clase ComentarioCreateView
        """
        try:
            form.instance.user = self.request.user
            form.instance.articulo_id = self.kwargs['pk']
            messages.success(self.request, 'Tu comentario fue publicado')
            return super(ComentarioCreateView, self).form_valid(form)
        except:
            return HttpResponseForbidden()
