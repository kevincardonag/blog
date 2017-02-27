from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from articulo.models import Articulo, Tag

from model_mommy import mommy


class ArticuloCreateViewTestCase(TestCase):
    """
    Autor: Kevin Cardona
    Fecha: 27 Febrero 2017
    prueba unitaria para la vista crear articulo
    """

    def setUp(self):
        self.categoria = mommy.make(Tag)

    def tearDown(self):
        del self.categoria

    def test_crear_articulo(self):
        """
        Autor: Kevin Cardona
        Fecha: 27 febrero 2017
        test crear articulo
        :return:
        """
        url = reverse('articulo:crear')
        datos = {
            'titulo': 'historia',
            'contenido': 'la historia de la tierra',
            'fecha_vencimiento': '2018-02-10',
            'tag': self.categoria.id,
        }
        self.assertEqual(Articulo.objects.count(), 0)
        response = self.client.post(url, datos)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Articulo.objects.count(), 1)


class IndexTestCase(TestCase):
    """
    Autor: Kevin Cardona
    Fecha: 27 Febrero 2017
    prueba unitaria para la vista Index(ListView),
    """

    def setUp(self):
        self.tags = mommy.make(Tag, _quantity=2)

    def tearDown(self):
        del self.tags

    def test_listar_categorias_index(self):
        """
        Autor: Kevin Cardona Giraldo
        Fecha: 27 Febrero 2017
        test listar articulos
        test para listar categorias en el index
        :return:
        """
        url = reverse('articulo:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ArticuloListViewTestCase(TestCase):
    """
    Autor: Kevin Cardona
    Fecha: 27 Febrero 2017
    prueba unitaria para la vista ArticuloListView(ListView),
    """

    def setUp(self):
        self.listado_articulos = mommy.make(Articulo, _quantity=3)

    def tearDown(self):
        del self.listado_articulos

    def test_listar_articulos(self):
        """
        Autor: Kevin Cardona Giraldo
        Fecha: 27 Febrero 2017
        test listar articulos
        test para listar articulos por categoria
        :return:
        """
        # si la categoria existe
        url = reverse('articulo:listar', kwargs={'id_tag': self.listado_articulos[0].id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class ArticuloDetailViewTestCase(TestCase):
    """
    Autor: Kevin Cardona
    Fecha: 27 febrero 2017
    prueba unitaria para la vista ArticuloDetailView
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.articulo = Articulo.objects.create(titulo='Historia', contenido='historia de la tierra',
                                                fecha_vencimiento='2019-09-11')

    def tearDown(self):
        del self.articulo

    def test_articulo_detalle(self):
        """
        Autor:Kevin Cardona
        Fecha: 27 Febrero 2017
        test para DetailView del modelo Articulo
        :return:
        """
        url = reverse('articulo:mostrar', kwargs={'pk': self.articulo.id})
        response = self.client.get(url)
        self.assertEqual(response.template_name[0], 'articulo/mostrar.html')
        self.assertEqual(response.context_data['object'], self.articulo)
        self.assertEqual(response.status_code, 200)

    def test_articulo_modificar(self):
        """
        Autor: Kevin Cardona
        Fecha: 27 Febrero 2017
        test para la vista UpdateView del modelo articulo
        :return:
        """
        url = reverse('articulo:editar', kwargs={'pk': self.articulo.id})
        response = self.client.post(url, {'titulo': "matemáticas", 'contenido': self.articulo.contenido,
                                          'fecha_vencimiento': self.articulo.fecha_vencimiento})
        self.assertEqual(response.status_code, 200)


class ComentarioCreateViewTestCase(TestCase):
    """
    Autor: Kevin Cardona
    Fecha: 27 Febrero 2017
    prueba unitaria para el modelo Comentario
    """

    def setUp(self):
        self.articulo = mommy.make(Articulo)

    def tearDown(self):
        del self.articulo

    def test_comentario_create(self):
        url = reverse('articulo:crear_comentario', kwargs={'pk': self.articulo.id})
        datos = {
            'comentario': 'muy buen post ',
            'articulo': self.articulo.id,
        }
        response = self.client.post(url, datos)
        self.assertEqual(response.status_code, 302)
