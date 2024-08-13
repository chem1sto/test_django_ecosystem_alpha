"""Модуль для работы с сериалайзерами приложения api."""

from django.conf import settings
from rest_framework import serializers
from rest_framework.request import Request
from store.models import Product, ProductCategory, ProductSubCategory


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
        fields = ["title", "slug"]


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели ProductCategory.

    Поля:
    - title: Название категории.
    - slug: Уникальный идентификатор категории.
    - product_subcategories: Список подкатегорий, связанных с данной
    категорией.
    """

    product_subcategories = ProductSubCategorySerializer(
        many=True, read_only=True
    )

    class Meta:
        """
        Мета-класс для ProductCategorySerializer.

        Атрибуты:
        - model: Модель ProductCategory.
        - fields: Поля модели, которые будут сериализованы (title, slug,
        product_subcategories).
        """

        model = ProductCategory
        fields = ("title", "slug", "product_subcategories")


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
        fields = (
            "title",
            "slug",
            "product_category",
            "product_subcategory",
            "price",
            "images",
        )

    def get_images(self, obj: Product) -> list:
        """
        Возвращает список URL-адресов изображений продукта.

        Параметры:
            obj (Product): Экземпляр модели Product.

        Возвращает:
            list: Список URL-адресов изображений.
        """
        request = self.context.get("request")
        if not isinstance(request, Request):
            return []
        base_url = request.build_absolute_uri(settings.MEDIA_URL)
        return [
            base_url + str(obj.image),
            base_url + str(obj.thumbnail),
            base_url + str(obj.preview),
        ]
