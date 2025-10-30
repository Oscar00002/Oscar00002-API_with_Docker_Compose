from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        # Especifica todos los campos del modelo que quieres exponer
        fields = ('id', 'nombre', 'descripcion', 'precio', 'disponible')

        # Alternativa -- fields = '__all__'