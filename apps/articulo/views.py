from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from apps.articulo.models import Articulo,Tag,Comentario
from apps.articulo.forms import articuloForm,comentarioForm
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
import json
import datetime
from django.core import serializers

# Create your views here.
def formularioCrearArticulo(request):
    if request.method == 'POST':
        form = articuloForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        form =articuloForm()
        return form
    else:
        form = articuloForm()
        return form

def index(request):
    form =formularioCrearArticulo(request)
    tags = Tag.objects.all()
    #numero de articulos
    numero_articulos = []
    i = 0
    for tag in tags:
        articulos = Articulo.objects.filter(tag__id=tag.id).filter(estado=True).filter(fecha_vencimiento__gte=datetime.datetime.now().date())
        cantidad_articulos = len(articulos)
        numero_articulos.append(cantidad_articulos)
        i=i+1
    lista=zip(tags,numero_articulos)
    return render(request,'admin/articulo/index.html',{'form':form,'lista':lista})

def listarArticulos(request,id_tag):
    articulos = Articulo.objects.filter(tag__id=id_tag).order_by('-fecha_publicacion').filter(estado=True)
    form = formularioCrearArticulo(request)
    return render(request, 'admin/articulo/listarArticulos.html', {'form': form,'articulos':articulos})

class mostrarArticulo(DetailView):
    model= Articulo
    template_name = 'admin/articulo/mostrar.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        pk=self.kwargs['pk']
        articulo=Articulo.objects.get(id=pk)
        context=super(mostrarArticulo, self).get_context_data(**kwargs)
        context['comentarios']=Comentario.objects.filter(articulo_id=pk)
        context['form'] = formularioCrearArticulo(self.request)
        context['form2']=articuloForm(instance=articulo)
        context['formComentario']= comentarioForm()
        context['id']=pk
        return context

    def get(self, request, *args, **kwargs):
        if(self.request.is_ajax()):
            id_articulo=self.request.GET.get('id')
            activado=self.request.GET.get('activado')
            articulo = Articulo.objects.get(id=id_articulo)
            if activado == '1':
                articulo.estado=False
                articulo.save()
                return HttpResponse('Estado: Desactivado')
            else:
                articulo.estado = True
                articulo.save()
                return HttpResponse('Estado: Desactivado')
            #data = serializers.serialize('json', articulo)
        return super(mostrarArticulo, self).get(request,*args, **kwargs)


def editarArticulo(request,id_articulo):
    articulo =Articulo.objects.get(id=id_articulo)

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
    form_class=comentarioForm
    second_form_class=articuloForm

    def get(self,request,*args,**kwargs):
        context=super(crearComentario, self).get(*args,**kwargs)
        if 'form' not in context:
            context['form']=articuloForm
        if 'formComentario' not in context:
            context['formComentario']=comentarioForm
        return context

    def post(self, request, *args, **kwargs):
        self.object =self.get_object
        formComentario= self.form_class(request.POST)
        form=self.second_form_class(request.POST)
        if formComentario.is_valid():
            id=kwargs['pk']
            comentario=formComentario.save(commit=False)
            comentario.articulo_id=id
            comentario.save()
            return redirect('articulo:index')


#class listarComentarios(ListView):
    #model=Comentario

