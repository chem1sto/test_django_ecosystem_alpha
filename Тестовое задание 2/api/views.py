"""Модуль для работы с представлениями приложения api."""

from api.pagination import ProductCategoryPagination, ProductPagination
from api.serializers import ProductCategorySerializer, ProductSerializer
from rest_framework import mixins, viewsets
from store.models import Product, ProductCategory


class ProductCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Предоставляет операцию чтения для модели ProductCategory.

    Операции:
    - просмотр списка категорий продуктов;

    Пагинация по умолчанию выводит по 5 категорий продуктов на странице.
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = ProductCategoryPagination


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Предоставляет операцию чтения для модели Product.

    Операции:
    - просмотр списка продуктов;

    Пагинация по умолчанию выводит по 10 продуктов на странице.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
