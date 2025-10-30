from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet

# Usamos un DefaultRouter para generar automáticamente las URLs CRUD (GET, POST, PUT, DELETE, etc.)
router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = router.urls
# Esto genera:
# productos/   (GET, POST)
# productos/{id}/ (GET, PUT, DELETE)