from django.conf.urls import url,include
from apps.articulo.views import index

urlpatterns = [
    url(r'^$',index),
]