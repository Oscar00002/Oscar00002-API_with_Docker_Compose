from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Producto

class ProductoAPITestCase(APITestCase):
    def setUp(self):
        # Crear producto para las pruebas 
        self.producto_data = {
            'nombre': 'Monitor 4K',
            'descripcion': 'Monitor de alta resolución.',
            'precio': '350.50',
            'disponible': True
        }
        self.list_url = reverse('producto-list') 

    def test_crear_producto(self):

        response = self.client.post(self.list_url, self.producto_data, format='json')
        
        # Verificar el código de estado
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verificar que el producto fue guardado en la DB
        self.assertEqual(Producto.objects.count(), 1)
        
        # 3. El nombre devuelto es correcto
        self.assertEqual(Producto.objects.get().nombre, 'Monitor 4K')
        

    def test_listar_productos_vacio(self):


        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
