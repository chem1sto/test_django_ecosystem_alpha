"""Настройки пагинации для представлений приложения api."""
from rest_framework import pagination
from rest_framework.response import Response


class ProductCategoryPagination(pagination.PageNumberPagination):
    """
    Пагинация для категорий продуктов.

    Параметры:
        page_size (int): Количество элементов на одной странице по умолчанию.
        page_size_query_param (str): Параметр запроса для указания количества
    элементов на странице.
    """

    page_size = 10
    page_size_query_param = "page_size"
