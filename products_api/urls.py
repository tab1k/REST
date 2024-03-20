from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'products_api'

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
print(router.urls)


urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:pk>/category/', ProductViewSet.as_view({'get': 'category'}), name='product-category'),

]




