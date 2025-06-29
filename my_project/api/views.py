from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(["GET"])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
