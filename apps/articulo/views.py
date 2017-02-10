from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import CreateView
from apps.articulo.models import Articulo
from apps.articulo.forms import articuloForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
def index(request):
    return render(request,'admin/articulo/index.html')
def crearArticulo(request):
    if request.method == 'POST':
        form = articuloForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('articulo:index')
    else:
        form= articuloForm()

    return render(request,'admin/articulo/index.html',{'form':form})
#class crearArticulo(CreateView):
 #   model = Articulo
    #fields=['titulo','contenido','imagen','fecha_publicacion','fecha_vencimiento']
  #  form_class = articuloForm
   # template_name = 'admin/articulo/index.html'
    #success_url = reverse_lazy('articulo:index')