"""
Модуль для настройки URL-адресов API.

Этот модуль содержит маршруты для API версии 1.
"""

from api.views import ProductCategoryViewSet, ProductViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register(
    r"product_categories",
    ProductCategoryViewSet,
    basename="product_categories",
)
router_v1.register(r"products", ProductViewSet, basename="products")

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
