"""Модуль для работы с сериалайзерами приложения api."""

from rest_framework import serializers
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
        fields = ["title", "slug", "product_subcategories"]


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Product.

    Поля:
    - title: Название продукта.
    - slug: Уникальный идентификатор продукта.
    - product_category: Категория продукта.
    - product_subcategory: Подкатегория продукта.
    - description: Описание продукта.
    - price: Цена продукта.
    """

    product_category = serializers.StringRelatedField()
    product_subcategory = serializers.StringRelatedField()

    class Meta:
        """
        Мета-класс для ProductSerializer.

        Атрибуты:
        - model: Модель Product.
        - exclude: Поля модели, которые не будут сериализованы (id,
        description).
        """

        model = Product
        exclude = ("id", "description")
