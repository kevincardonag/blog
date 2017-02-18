from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseRedirect
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from apps.articulo.models import Articulo,Tag
from apps.articulo.forms import articuloForm
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
import json
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
    numero_articulos = []
    i = 0
    for tag in tags:
        articulos = Articulo.objects.filter(tag__id=tag.id)
        cantidad_articulos = len(articulos)
        numero_articulos.append(cantidad_articulos)
        i=i+1
    lista=zip(tags,numero_articulos)
    return render(request,'admin/articulo/index.html',{'form':form,'lista':lista})

def listarArticulos(request,id_tag):
    articulos = Articulo.objects.filter(tag__id=id_tag).order_by('-fecha_publicacion')
    form = formularioCrearArticulo(request)
    return render(request, 'admin/articulo/listarArticulos.html', {'form': form,'articulos':articulos})

class mostrarArticulo(DetailView):
    model= Articulo
    template_name = 'admin/articulo/mostrar.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context=super(mostrarArticulo, self).get_context_data(**kwargs)
        context['cometarios']=Articulo.objects.filter(id='11')
        context['form']=formularioCrearArticulo(self.request)
        return context

    def get(self, request, *args, **kwargs):
        if(self.request.is_ajax()):
            id_articulo=self.request.GET.get('id')
            articulo = Articulo.objects.filter(id=id_articulo)
            data = serializers.serialize('json', articulo)
            return HttpResponse(data)
        return super(mostrarArticulo, self).get(request,*args, **kwargs)

def editarArticulo(request,id_articulo):
    articulo =Articulo.objects.get(id=id_articulo)

    if request.method == 'GET':
        form = articuloForm(instance=articulo)
    else :
        form=articuloForm(request.POST,instance=articulo)
        return HttpResponse({request.POST.get('tag')})
        if form.is_valid():
            form.save()
        return redirect('articulo:index')
    return HttpResponse('si')

"""class editarArticulo(UpdateView):
    model=Articulo
    form_class = articuloForm
    template_name = 'admin/articulo/mostrar.html'
    success_url = reverse_lazy('articulo:index')"""

#class crearArticulo(CreateView):
 #   model = Articulo
    #fields=['titulo','contenido','imagen','fecha_publicacion','fecha_vencimiento']
  #  form_class = articuloForm
   # template_name = 'admin/articulo/index.html'
    #success_url = reverse_lazy('articulo:index')