from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from articulo.models import Articulo, Tag
from model_mommy import mommy


class ArticuloCreateViewTestCase(TestCase):
    """
    Autor: Kevin Cardona
    Fecha: 27 Febrero 2017
    prueba unitaria para la vista crear articulo
    """

    def setUp(self):
        self.user = mommy.make(User)
        self.user.set_password('123456')
        self.user.save()
        self.categoria = mommy.make(Tag)
        self.datos = {
            'titulo': 'historia',
            'contenido': 'la historia de la tierra',
            'fecha_vencimiento': '2018-02-10',
            'tag': self.categoria.id,
        }

    def tearDown(self):
        del self.categoria
        del self.user
        del self.datos

    def test_crear_articulo_user_no_authenticated(self):
        """
        Autor: Kevin Cardona
        Fecha: 27 febrero 2017
        test crear articulo cuando un usuario no esta autenticado
        :return: retorna True si el usuario no esta autenticado
        """
        url = reverse('articulo:crear')
        response = self.client.post(url, self.datos)
        print(response.url)
        self.assertEqual(response.status_code, 302)

    def test_crear_articulo_user_authenticated(self):
        """
        Autor: Kevin Cardona
        Fecha: 2 de marzo 2015
        test para crear articulos cuando existe un usuario autenticado
        :return: retorna True si el articulo fue creado con exito
        """
        login = self.client.login(username=self.user.username, password='123456')
        url = reverse('articulo:crear')

        self.assertEqual(Articulo.objects.count(), 0)
        response = self.client.post(url, self.datos)

        self.assertTrue(login)
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
        self.user = mommy.make(User)
        self.user.set_password('123456')
        self.user.save()

    def tearDown(self):
        del self.articulo
        del self.user

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

    def test_articulo_modificar_user_no_autheticated(self):
        """
        Autor: Kevin Cardona
        Fecha: 27 Febrero 2017
        test para la vista UpdateView del modelo articulo cuando un usuario no esta autenticado
        :return:
        """
        url = reverse('articulo:editar', kwargs={'pk': self.articulo.id})
        response = self.client.post(url, {'titulo': "matemáticas", 'contenido': self.articulo.contenido,
                                          'fecha_vencimiento': self.articulo.fecha_vencimiento})
        self.assertEqual(response.status_code, 302)

    def test_articulo_modificar_user_autheticated(self):
        """
        Autor: Kevin Cardona
        Fecha: 4 de marzo 2017
        test para la vista UpdateView del modelo articulo cuando un usuario esta autenticado
        :return:
        """
        login = self.client.login(username=self.user.username, password='123456')
        url = reverse('articulo:editar', kwargs={'pk': self.articulo.id})
        response = self.client.post(url, {'titulo': "matemáticas", 'contenido': self.articulo.contenido,
                                          'fecha_vencimiento': self.articulo.fecha_vencimiento})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(login)


class ComentarioCreateViewTestCase(TestCase):
    """
    Autor: Kevin Cardona
    Fecha: 27 Febrero 2017
    prueba unitaria para el modelo Comentario
    """

    def setUp(self):
        self.articulo = mommy.make(Articulo)
        self.user = mommy.make(User)
        self.user.set_password('123456')
        self.user.save()
        self.datos = {
            'comentario': 'muy buen post',
            'articulo': self.articulo.id,
            'user': self.user.id,
        }

    def tearDown(self):
        del self.articulo

    def test_comentario_create_user_no_authenticated(self):
        """
        Autor:Kevin Cardona Giraldo
        Fecha: 2 de marzo 2017
        test encargado de verificar la creacion de un comentario con un usuario no autenticado.
        :return retorna true si el usuario no esta autenticado :
        """
        url = reverse('articulo:crear-comentario', kwargs={'pk': self.articulo.id})
        response = self.client.post(url, self.datos)
        self.assertEqual(response.status_code, 403)

    def test_comentario_create_user_authenticated(self):
        """
        Autor: Kevin Cardona
        Fecha: 2 Marzo de 2017
        test encargado de verificar la creacion de un comentario cuando el usuario esta autenticado
        :return: retorna un True si el usuario esta auntenticado y puede crear el comentario
        """
        login = self.client.login(username=self.user.username, password='123456')

        url = reverse('articulo:crear-comentario', kwargs={'pk': self.articulo.id})
        response = self.client.post(url, self.datos)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(login)
