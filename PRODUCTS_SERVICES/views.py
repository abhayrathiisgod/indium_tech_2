from django.shortcuts import render
from .models import Product, SERVICES
from .serializers import ProductSerializer, ServicesSerializer
from rest_framework import generics
# Create your views here.


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ServiceView(generics.ListAPIView):
    queryset = SERVICES.objects.all()
    serializer_class = ServicesSerializer
