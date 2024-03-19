from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from .models import Product, Category
from .serializers import *


# class ProductAPIView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'price']
