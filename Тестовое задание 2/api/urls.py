"""
Модуль для настройки URL-адресов API.

Этот модуль содержит маршруты для API версии 1.
"""

from api.views import (
    CartViewSet,
    CustomObtainAuthToken,
    ProductCategoryViewSet,
    ProductViewSet,
)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register(
    prefix=r"product_categories",
    viewset=ProductCategoryViewSet,
    basename="product_categories",
)
router_v1.register(
    prefix=r"products", viewset=ProductViewSet, basename="products"
)
router_v1.register(prefix=r"cart", viewset=CartViewSet, basename="cart")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path(
        "v1/api-token-auth/",
        CustomObtainAuthToken.as_view(),
        name="api_token_auth",
    ),
]
