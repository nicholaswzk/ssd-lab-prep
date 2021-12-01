from django.test import TestCase, Client
from django.urls import reverse, resolve
from ..views import home, login, register


class Test_NonUserRequired_Urls(TestCase):


    def setUp(self):
        super().setUp()
        self.client = Client()

    def test_index_url(self):
        """
            A non authenticated user tries to access index page

            The user will be redirected to index page
        """
        url = reverse('index')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func, home)
        self.assertTemplateUsed(response, 'index.html')

    def test_login_url(self):
        """
            A non authenticated user tries to access login page

            The user will be redirected to login page
        """
        url = reverse('login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func, login)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_url(self):
        """
            A non authenticated user tries to access register page

            The user will be redirected to register page
        """
        url = reverse('register')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(resolve(url).func, register)
        self.assertTemplateUsed(response, 'register.html')