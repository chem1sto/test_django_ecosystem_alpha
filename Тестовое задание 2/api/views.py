"""Модуль для работы с представлениями приложения api."""

from api.pagination import ProductCategoryPagination
from api.serializers import ProductCategorySerializer
from rest_framework import mixins, permissions, status, viewsets
from store.models import ProductCategory


class ProductCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Предоставляет операции чтения для модели ProductCategory.

    Операции:
    - просмотр списка категорий продуктов;
    - просмотр деталей категории продуктов.

    Пагинация настроена на 10 элементов на странице.
    Поиск объектов осуществляется по полю `slug`.
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = ProductCategoryPagination
    lookup_field = "slug"
