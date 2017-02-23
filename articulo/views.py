from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.http import JsonResponse

from django.views.generic import CreateView, ListView, DetailView, UpdateView
from articulo.models import Articulo, Tag, Comentario
from articulo.forms import articuloForm, comentarioForm

import json
import datetime


class ArticuloCreateView(CreateView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase CreateView, para la creacion de articulos
    """
    model = Articulo
    template_name='admin/articulo/crearArticulo.html'
    form_class=articuloForm
    success_url=reverse_lazy('articulo:index')


class index(ListView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase index, se lista todas las categorias(Tags) y cantidad de articulos por cada categoria
    """
    model = Tag
    template_name = 'admin/articulo/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['info_articulos'] = Tag.custom_objects.obtener_cantidad_articulos_por_categoria()
        return context


class ArticuloListView(ListView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase ListView, encargada de listar los articulos por una categoria
    """
    model = Articulo
    template_name = 'admin/articulo/listarArticulos.html'

    def get_context_data(self, **kwargs):
        context = super(ArticuloListView, self).get_context_data(**kwargs)
        context['articulos'] = Articulo.objects.filter(tag__id=self.kwargs['id_tag'], estado=True).order_by('-fecha_publicacion')
        return context


class ArticuloDetailView(DetailView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase DetailView, muestra un articulo en detalle
    """
    model = Articulo
    template_name = 'admin/articulo/mostrar.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context =super(ArticuloDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs['pk']
        articulo = Articulo.objects.get(id=pk)
        context['comentarios'] = Comentario.objects.filter(articulo_id=pk)
        context['form2'] = articuloForm(instance=articulo)
        context['formComentario'] = comentarioForm()
        context['id'] = pk
        return context

    def get(self, request, *args, **kwargs):
        if(self.request.is_ajax()):
            id_articulo = self.request.GET.get('id')
            activado = self.request.GET.get('activado')
            articulo = Articulo.objects.get(id = id_articulo)
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
    form_class = articuloForm
    success_url = reverse_lazy('articulo:index')


class ComentarioCreateView(CreateView):
    """
    Autor: Kevin Cardona
    Fecha: 23 de febrero 2017
    clase CreateView, para la creacion de comentarios
    """
    model = Comentario
    template_name = 'admin/articulo/mostrar.html'
    form_class = comentarioForm
    second_form_class = articuloForm

    def get(self, request, *args, **kwargs):
        context=super(ComentarioCreateView, self).get(*args, **kwargs)
        if 'form' not in context:
            context['form'] = articuloForm
        if 'formComentario' not in context:
            context['formComentario'] = comentarioForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        formComentario = self.form_class(request.POST)
        form = self.second_form_class(request.POST)
        if formComentario.is_valid():
            id = kwargs['pk']
            comentario = formComentario.save(commit=False)
            comentario.articulo_id = id
            comentario.save()
            return redirect('articulo:index')