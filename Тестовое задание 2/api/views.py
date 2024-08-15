"""Модуль для работы с представлениями приложения api."""

from api.pagination import ProductCategoryPagination, ProductPagination
from api.serializers import (
    CartItemSerializer,
    CartSerializer,
    ProductCategorySerializer,
    ProductSerializer,
    ShortCartItemSerializer,
)
from core.constants import TOKEN, USERNAME, ProductSubCategoryCfg, ViewsCfg
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from store.models import Cart, CartItem, Product, ProductCategory


class CustomObtainAuthToken(ObtainAuthToken):
    """
    Кастомное представление для получения аутентификационного токена.

    Это представление расширяет ObtainAuthToken для возврата токена вместе с
    именем пользователя.
    """

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Обработка POST-запросов для получения аутентификационного токена.

        Параметры:
            request (HttpRequest): Входящий HTTP-запрос.
            *args: Список аргументов переменной длины.
            **kwargs: Произвольные именованные аргументы.

        Возвращает:
            Response: JSON-ответ, содержащий аутентификационный токен и имя
        пользователя
        """
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs
        )
        token = Token.objects.get(key=response.data[TOKEN])
        return Response({TOKEN: token.key, USERNAME: token.user.username})


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

    Требуется аутентификация пользователя по токену.
    """

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self) -> Cart:
        """
        Возвращает корзину текущего пользователя.

        Если корзина не существует, создает новую.

        Возвращает:
            Cart: Корзина текущего пользователя.
        """
        return Cart.objects.get_or_create(user=self.request.user)[0]

    def list(self, request: Request) -> Response:
        """
        Возвращает содержимое корзины текущего пользователя.

        Возвращает также подсчёт количества товара и сумму их стоимости.

        Возвращает:
            Response: Сериализованное содержимое корзины.
        """
        cart = self.get_queryset()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @staticmethod
    def get_product(product_title: str) -> Product | ValidationError:
        """
        Возвращает продукт по его наименованию.

        Параметры:
            product_title (str): Наименование продукта.

        Возвращает:
            Product: Объект продукта.

        Вызывает ошибку:
            ValidationError: Если продукт с указанным наименованием не
        существует.
        """
        try:
            return Product.objects.get(title=product_title)
        except Product.DoesNotExist:
            raise ValidationError(
                detail=ViewsCfg.GET_PRODUCT_VALIDATION_ERROR.format(
                    product_title=product_title
                ),
                code=status.HTTP_404_NOT_FOUND,
            )

    @staticmethod
    def get_cart_item(
        cart: Cart, product: Product
    ) -> CartItem | ValidationError:
        """
        Возвращает элемент корзины по корзине и продукту.

        Параметры:
            cart (Cart): Корзина пользователя.
            product (Product): Продукт.

        Возвращает:
            CartItem: Элемент корзины.

        Вызывает ошибку:
            ValidationError: Если элемент корзины с указанным продуктом не
        существует.
        """
        try:
            return CartItem.objects.get(cart=cart, product=product)
        except CartItem.DoesNotExist:
            raise ValidationError(
                detail=ViewsCfg.CART_ITEM_VALIDATION_ERROR.format(
                    product=product.title
                ),
                code=status.HTTP_404_NOT_FOUND,
            )

    @swagger_auto_schema(
        request_body=CartItemSerializer,
    )
    @action(detail=False, methods=ViewsCfg.ADD_ITEM_HTTP_METHODS)
    def add_item(self, request: Request) -> Response:
        """
        Добавляет товар в корзину текущего пользователя.

        Параметры запроса:
        - product: Наименование продукта.
        - quantity: Количество продукта (по умолчанию 1).

        Возвращает:
            Response: Сериализованное содержимое корзины после добавления
        товара.
        """
        product = self.get_product(request.data.get(ViewsCfg.PRODUCT))
        cart = self.get_queryset()
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product
        )
        cart_item.quantity += int(
            request.data.get(
                ViewsCfg.QUANTITY, ViewsCfg.QUANTITY_DEFAULT_VALUE
            )
        )
        cart_item.save()
        return Response(CartSerializer(cart).data)

    @swagger_auto_schema(
        request_body=ShortCartItemSerializer,
    )
    @action(detail=False, methods=ViewsCfg.REMOVE_ITEM_HTTP_METHODS)
    def remove_item(self, request: Request) -> Response:
        """
        Удаляет товар из корзины текущего пользователя.

        Параметры запроса:
        - product: Наименование продукта.

        Возвращает:
            Response: Сериализованное содержимое корзины после удаления товара.
        """
        cart = self.get_queryset()
        product = self.get_product(
            product_title=request.data.get(ViewsCfg.PRODUCT)
        )
        cart_item = self.get_cart_item(cart=cart, product=product)
        cart_item.delete()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CartItemSerializer,
    )
    @action(detail=False, methods=ViewsCfg.UPDATE_ITEM_HTTP_METHODS)
    def update_item(self, request: Request) -> Response:
        """
        Обновляет количество товара в корзине текущего пользователя.

        Параметры запроса:
        - product: Наименование продукта.
        - quantity: Новое количество продукта.

        Возвращает:
            Response: Сериализованное содержимое корзины после обновления
        количества товара.
        """
        cart = self.get_queryset()
        product = self.get_product(request.data.get(ViewsCfg.PRODUCT))
        cart_item = self.get_cart_item(cart=cart, product=product)
        quantity = request.data.get(ViewsCfg.QUANTITY)
        cart_item.quantity = quantity
        cart_item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=ViewsCfg.CLEAR_CART_HTTP_METHODS)
    def clear_cart(self, request: Request) -> Response:
        """
        Полностью очищает корзину текущего пользователя.

        Возвращает:
            Response: Сериализованное содержимое пустой корзины.
        """
        cart = self.get_queryset()
        cart.items.all().delete()
        serializer = CartSerializer(cart)
        return Response(serializer.data)
