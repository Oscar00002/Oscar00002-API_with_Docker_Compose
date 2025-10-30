from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    # Consulta la lista de productos disponibles
    queryset = Producto.objects.all() 
    # Usa  serializador
    serializer_class = ProductoSerializer