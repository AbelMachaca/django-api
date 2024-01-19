
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Producto

def listar_productos(request):
    productos = Producto.objects.all()
    data = {'productos': [{'nombre': producto.nombre, 'descripcion': producto.descripcion} for producto in productos]}
    return JsonResponse(data)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    data = {'nombre': producto.nombre, 'descripcion': producto.descripcion}
    return JsonResponse(data)
