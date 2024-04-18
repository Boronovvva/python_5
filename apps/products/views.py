from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from apps.products.models import Product
from apps.products.serializers import ProductSerializer
# Create your views here.

class ProductViewSet(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer