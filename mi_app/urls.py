
from django.urls import path
from .views import listar_productos, detalle_producto

urlpatterns = [
    path('productos/', listar_productos, name='listar_productos'),
    path('productos/<int:producto_id>/', detalle_producto, name='detalle_producto'),
]
