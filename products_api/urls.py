from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'category', CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(router.urls)),

]


