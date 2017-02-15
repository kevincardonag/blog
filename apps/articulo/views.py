from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from apps.articulo.models import Articulo,Tag
from apps.articulo.forms import articuloForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def formularioCrearArticulo(request):
    if request.method == 'POST':
        form = articuloForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('articulo:index')
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
    articulos = Articulo.objects.filter(tag__id=id_tag)
    form = formularioCrearArticulo(request)
    return render(request, 'admin/articulo/listarArticulos.html', {'form': form,'articulos':articulos})

def mostrarArticulo(request,id_articulo):
    articulo= Articulo.objects.find(id_articulo)
    form = formularioCrearArticulo(request)
    return render(request, 'admin/articulo/listarArticulos.html', {'form': form, 'articulo': articulo})


#class crearArticulo(CreateView):
 #   model = Articulo
    #fields=['titulo','contenido','imagen','fecha_publicacion','fecha_vencimiento']
  #  form_class = articuloForm
   # template_name = 'admin/articulo/index.html'
    #success_url = reverse_lazy('articulo:index')