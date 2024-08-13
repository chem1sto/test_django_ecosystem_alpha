"""
Модуль для настройки URL-адресов API.

Этот модуль содержит маршруты для API версии 1.
"""

from api.views import ProductCategoryViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register(
    r"product_category", ProductCategoryViewSet, basename="product_category"
)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
]
