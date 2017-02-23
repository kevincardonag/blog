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


class Crear_articulo(CreateView):
    model = Articulo
    template_name='admin/articulo/crearArticulo.html'
    form_class=articuloForm
    success_url=reverse_lazy('articulo:index')


class index(ListView):
    model = Tag
    template_name = 'admin/articulo/index.html'
    
    def get_context_data(self, **kwargs):
        context = super(index, self).get_context_data(**kwargs)
        context['info_articulos'] = Tag.custom_objects.obtener_cantidad_articulos_por_categoria()
        return context


class Listar_articulos(ListView):
    model = Articulo
    template_name = 'admin/articulo/listarArticulos.html'

    def get_context_data(self, **kwargs):
        context = super(Listar_articulos, self).get_context_data(**kwargs)
        context['articulos'] = Articulo.objects.filter(tag__id=self.kwargs['id_tag'], estado=True).order_by('-fecha_publicacion')
        return context


class mostrarArticulo(DetailView):
    model = Articulo
    template_name = 'admin/articulo/mostrar.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context =super(mostrarArticulo, self).get_context_data(**kwargs)
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
        return super(mostrarArticulo, self).get(request,*args, **kwargs)


def editarArticulo(request,id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)

    if request.method == 'GET':
        form = articuloForm(instance=articulo)
    else :
        form=articuloForm(request.POST,instance=articulo)
        if form.is_valid():
            form.save()
        return redirect('articulo:index')

    return HttpResponse('si')



class crearComentario(CreateView):
    model = Comentario
    template_name = 'admin/articulo/mostrar.html'
    form_class = comentarioForm
    second_form_class = articuloForm

    def get(self, request, *args, **kwargs):
        context=super(crearComentario, self).get(*args, **kwargs)
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



