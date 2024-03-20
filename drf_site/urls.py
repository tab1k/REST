from django.contrib import admin
from django.urls import path, include, re_path
from djoser.views import TokenCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),

    # DJANGO DEFAULT PAGE
    path('', include('startapp.urls')),

    # API APP
    path("api/", include("products_api.urls")),

    # DJOSER
    path("api/auth/", include("djoser.urls")),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    # JWT
    path('api/auth/token/', TokenCreateView.as_view(), name='token_create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)