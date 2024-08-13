"""Модуль для работы с представлениями приложения api."""

from api.pagination import ProductCategoryPagination, ProductPagination
from api.serializers import (
    CartItemSerializer,
    CartSerializer,
    ProductCategorySerializer,
    ProductSerializer,
)
from core.constants import ProductSubCategoryCfg
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from store.models import Cart, CartItem, Product, ProductCategory


class ProductCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Предоставляет операцию чтения для модели ProductCategory.

    Операции:
    - просмотр списка категорий продуктов с подкатегориями;

    Пагинация по умолчанию выводит по 5 категорий продуктов на странице.
    """

    queryset = ProductCategory.objects.all().prefetch_related(
        ProductSubCategoryCfg.PRODUCT_CATEGORY_RELATED_NAME
    )
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


class CartViewSet(viewsets.ViewSet):
    """
    Предоставляет операции для работы с корзиной пользователя.

    Операции:
    - просмотр содержимого корзины;
    - добавление товара в корзину;
    - удаление товара из корзины;
    - обновление количества товара в корзине.

    Требуется аутентификация пользователя.
    """

    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """
        Возвращает корзину текущего пользователя.

        Если корзина не существует, создает новую.

        Возвращает:
            Cart: Корзина текущего пользователя.
        """
        return Cart.objects.get_or_create(user=self.request.user)[0]

    def list(self, request):
        """
        Возвращает содержимое корзины текущего пользователя.

        Возвращает:
            Response: Сериализованное содержимое корзины.
        """
        cart = self.get_object()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CartItemSerializer,
    )
    @action(detail=False, methods=["post"])
    def add_item(self, request):
        """
        Добавляет товар в корзину текущего пользователя.

        Параметры запроса:
        - product: Название продукта.
        - quantity: Количество продукта (по умолчанию 1).

        Возвращает:
            Response: Сериализованное содержимое корзины после добавления
        товара.

        Возбуждает:
            ValidationError: Если продукт с указанным названием не существует.
        """
        cart = self.get_object()
        product_title = request.data.get("product")
        try:
            product = Product.objects.get(title=product_title)
        except Product.DoesNotExist:
            raise ValidationError(
                f"Product with title {product_title} does not exist."
            )
        quantity = request.data.get("quantity", 1)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )
        cart_item.quantity += int(quantity)
        cart_item.save()
        return Response(CartSerializer(cart).data)

    @swagger_auto_schema(
        request_body=CartItemSerializer,
    )
    @action(detail=False, methods=["delete"])
    def remove_item(self, request):
        """
        Удаляет товар из корзины текущего пользователя.

        Параметры запроса:
        - product_id: Идентификатор продукта.

        Возвращает:
            Response: Сериализованное содержимое корзины после удаления товара.

        Вызывает ошибку:
            Response: Если товар не найден, возвращает статус 404.
        """
        cart = self.get_object()
        product_id = request.data.get("product_id")
        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except CartItem.DoesNotExist:
            return Response(
                {"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )

    @swagger_auto_schema(
        request_body=CartItemSerializer,
    )
    @action(detail=False, methods=["patch"])
    def update_item(self, request):
        """
        Обновляет количество товара в корзине текущего пользователя.

        Параметры запроса:
        - product_id: Идентификатор продукта.
        - quantity: Новое количество продукта.

        Возвращает:
            Response: Сериализованное содержимое корзины после обновления
        количества товара.

        Вызывает ошибку:
            Response: Если товар не найден, возвращает статус 404.
        """
        cart = self.get_object()
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")
        try:
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.quantity = quantity
            cart_item.save()
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except CartItem.DoesNotExist:
            return Response(
                {"detail": "Item not found"}, status=status.HTTP_404_NOT_FOUND
            )
