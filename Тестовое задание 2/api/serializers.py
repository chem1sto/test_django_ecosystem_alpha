"""Модуль для работы с сериалайзерами приложения api."""

from core.constants import REQUEST, SerializersCfg
from django.conf import settings
from rest_framework import serializers
from rest_framework.request import Request
from store.models import (
    Cart,
    CartItem,
    Product,
    ProductCategory,
    ProductSubCategory,
)


class ProductSubCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ProductSubCategory.

    Поля:
    - title: Название подкатегории.
    - slug: Уникальный идентификатор подкатегории.
    """

    class Meta:
        """
        Мета-класс для ProductSubCategorySerializer.

        Атрибуты:
        - model: Модель ProductSubCategory.
        - fields: Поля модели, которые будут сериализованы (title, slug).
        """

        model = ProductSubCategory
        fields = SerializersCfg.PRODUCT_SUBCATEGORY_SERIALIZER_META_FIELDS


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ProductCategory.

    Поля:
    - title: Название категории.
    - slug: Уникальный идентификатор категории.
    - product_subcategories: Список подкатегорий, связанных с данной
    категорией.
    """

    subcategories = ProductSubCategorySerializer(many=True, read_only=True)

    class Meta:
        """
        Мета-класс для ProductCategorySerializer.

        Атрибуты:
        - model: Модель ProductCategory.
        - fields: Поля модели, которые будут сериализованы (title, slug,
        product_subcategories).
        """

        model = ProductCategory
        fields = SerializersCfg.PRODUCT_CATEGORY_SERIALIZER_META_FIELDS


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Поля:
    - title: Название продукта.
    - slug: Уникальный идентификатор продукта.
    - product_category: Категория продукта.
    - product_subcategory: Подкатегория продукта.
    - price: Цена продукта.
    - images: Список URL-адресов изображений продукта.
    """

    product_category = serializers.StringRelatedField()
    product_subcategory = serializers.StringRelatedField()
    images = serializers.SerializerMethodField()

    class Meta:
        """
        Мета-класс для ProductSerializer.

        Атрибуты:
        - model: Модель Product.
        - fields: Поля модели, которые будут сериализованы (title, slug,
        product_category, product_subcategory, price, images).
        """

        model = Product
        fields = SerializersCfg.PRODUCT_SERIALIZER_META_FIELDS

    def get_images(self, obj: Product) -> list:
        """
        Возвращает список URL-адресов изображений продукта.

        Параметры:
            obj (Product): Экземпляр модели Product.

        Возвращает:
            list: Список URL-адресов изображений.
        """
        request = self.context.get(REQUEST)
        if not isinstance(request, Request):
            return []
        base_url = request.build_absolute_uri(settings.MEDIA_URL)
        return [
            base_url + str(obj.image),
            base_url + str(obj.thumbnail),
            base_url + str(obj.preview),
        ]


class CartItemSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели CartItem.

    Поля:
    - product: Название продукта.
    - quantity: Количество продукта в корзине.
    """

    product = serializers.CharField(source="product.title")
    quantity = serializers.IntegerField(default=1)

    class Meta:
        """
        Мета-класс для CartItemSerializer.

        Атрибуты:
        - model: Модель CartItem.
        - fields: Поля модели, которые будут сериализованы (product, quantity).
        """

        model = CartItem
        fields = SerializersCfg.CART_ITEM_SERIALIZER_META_FIELDS


class CartSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Cart.

    Поля:
    - user: Имя пользователя.
    - items: Список элементов корзины.
    """

    user = serializers.StringRelatedField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        """
        Мета-класс для CartSerializer.

        Атрибуты:
        - model: Модель Cart.
        - fields: Поля модели, которые будут сериализованы (user, items).
        """

        model = Cart
        fields = SerializersCfg.CART_SERIALIZER_META_FIELDS
