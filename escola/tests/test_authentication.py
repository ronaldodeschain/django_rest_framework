from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username='admin',
            password='admin',
            email='email@email'
        )

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Test que verifica credenciais corretas do user"""
        usuario = authenticate(username='admin',password='admin')
        self.assertTrue((usuario is not None )and usuario.is_authenticated)
    
    def test_autenticacao_user_com_credenciais_incorretas(self):
        """Test que verifica credenciais incorretas do user"""
        usuario = authenticate(username='admn',password='admin')
        self.assertFalse((usuario is not None )and usuario.is_authenticated)
