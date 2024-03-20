from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, get_object_or_404, ListCreateAPIView, RetrieveUpdateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from .models import Product, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import *


class ProductAPIViewPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ProductAPIViewPagination


class ProductAPIUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, ]


class ProductAPIDelete(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (OrderingFilter, SearchFilter)
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'price']

    def get_permissions(self):
        if self.action in ['create', 'list']:
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        elif self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


    @action(methods=['get'], detail=False)
    def category(self, request, pk=None):
        if pk is not None:
            category = get_object_or_404(Category, pk=pk)
            return Response({
                'category': category.name,
            })
        else:
            categories = Category.objects.all()
            category_names = [category.name for category in categories]
            return Response({
                'categories': category_names,
            })