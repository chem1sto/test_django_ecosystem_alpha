"""Модуль для определения моделей приложения store."""

from core.constants import (
    BaseProductCategoryCfg,
    ProductCategoryCfg,
    ProductCfg,
    ProductSubCategoryCfg,
)
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class BaseProductCategory(models.Model):
    """
    Абстрактная базовая модель для категорий продуктов.

    Содержит общие поля для категорий и подкатегорий продуктов.
    """

    title = models.CharField(
        max_length=BaseProductCategoryCfg.TITLE_MAX_LENGTH,
        verbose_name=BaseProductCategoryCfg.TITLE_VERBOSE_NAME,
        help_text=BaseProductCategoryCfg.TITLE_HELP_TEXT,
    )
    slug = models.SlugField(
        max_length=BaseProductCategoryCfg.SLUG_MAX_LENGTH,
        help_text=BaseProductCategoryCfg.SLUG_HELP_TEXT,
        allow_unicode=True,
        unique=True,
    )
    description = models.TextField(
        max_length=BaseProductCategoryCfg.DESCRIPTION_MAX_LENGTH,
        verbose_name=BaseProductCategoryCfg.DESCRIPTION_VERBOSE_NAME,
        help_text=BaseProductCategoryCfg.DESCRIPTION_HELP_TEXT,
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to=BaseProductCategoryCfg.IMAGE_UPLOAD_FOLDER,
        verbose_name=BaseProductCategoryCfg.IMAGE_VERBOSE_NAME,
        help_text=BaseProductCategoryCfg.IMAGE_HELP_TEXT,
    )

    class Meta:
        """Мета-класс для абстрактной базовой модели категорий продуктов."""

        abstract = True

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.title


class ProductCategory(BaseProductCategory):
    """
    Модель для категорий продуктов.

    Наследует общие поля от BaseProductCategory.
    """

    pass

    class Meta:
        """Мета-класс для модели категорий продуктов."""

        ordering = ProductCategoryCfg.PRODUCT_CATEGORY_ORDER
        verbose_name = ProductCategoryCfg.VERBOSE_NAME
        verbose_name_plural = ProductCategoryCfg.VERBOSE_NAME_PLURAL


class ProductSubCategory(BaseProductCategory):
    """
    Модель для подкатегорий продуктов.

    Наследует общие поля от BaseProductCategory и добавляет связь с категорией.
    """

    title = models.CharField(
        max_length=ProductSubCategoryCfg.TITLE_MAX_LENGTH,
        verbose_name=ProductSubCategoryCfg.TITLE_VERBOSE_NAME,
        help_text=ProductSubCategoryCfg.TITLE_HELP_TEXT,
    )
    description = models.TextField(
        max_length=ProductSubCategoryCfg.DESCRIPTION_MAX_LENGTH,
        verbose_name=ProductSubCategoryCfg.DESCRIPTION_VERBOSE_NAME,
        help_text=ProductSubCategoryCfg.DESCRIPTION_HELP_TEXT,
    )
    image = models.ImageField(
        upload_to=ProductSubCategoryCfg.IMAGE_UPLOAD_FOLDER,
        verbose_name=ProductSubCategoryCfg.IMAGE_VERBOSE_NAME,
        help_text=ProductSubCategoryCfg.IMAGE_HELP_TEXT,
    )
    product_category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
        related_name=ProductSubCategoryCfg.PRODUCT_CATEGORY_RELATED_NAME,
        verbose_name=ProductSubCategoryCfg.PRODUCT_CATEGORY_VERBOSE_NAME,
        help_text=ProductSubCategoryCfg.PRODUCT_CATEGORY_HELP_TEXT,
    )

    class Meta:
        """Мета-класс для модели подкатегорий продуктов."""

        verbose_name = ProductSubCategoryCfg.VERBOSE_NAME
        verbose_name_plural = ProductSubCategoryCfg.VERBOSE_NAME_PLURAL


class Product(models.Model):
    """
    Модель для продуктов.

    Содержит информацию о продукте, включая категорию, подкатегорию, цену и
    изображение.
    """

    title = models.CharField(
        max_length=ProductCfg.TITLE_MAX_LENGTH,
        verbose_name=ProductCfg.TITLE_VERBOSE_NAME,
        help_text=ProductCfg.TITLE_HELP_TEXT,
    )
    slug = models.SlugField(
        max_length=ProductCfg.SLUG_MAX_LENGTH,
        allow_unicode=True,
        unique=True,
    )
    description = models.TextField(
        max_length=ProductCfg.DESCRIPTION_MAX_LENGTH,
        verbose_name=ProductCfg.DESCRIPTION_VERBOSE_NAME,
        help_text=ProductCfg.DESCRIPTION_HELP_TEXT,
        blank=True,
        null=True,
    )
    product_category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
        related_name=ProductCfg.PRODUCT_CATEGORY_RELATED_NAME,
        verbose_name=ProductCfg.PRODUCT_CATEGORY_VERBOSE_NAME,
        help_text=ProductCfg.PRODUCT_CATEGORY_HELP_TEXT,
    )
    product_subcategory = models.ForeignKey(
        to=ProductSubCategory,
        on_delete=models.CASCADE,
        related_name=ProductCfg.PRODUCT_SUBCATEGORY_RELATED_NAME,
        verbose_name=ProductCfg.PRODUCT_SUBCATEGORY_VERBOSE_NAME,
        help_text=ProductCfg.PRODUCT_SUBCATEGORY_HELP_TEXT,
    )
    price = models.DecimalField(
        max_digits=ProductCfg.PRICE_MAX_DIGITS,
        decimal_places=ProductCfg.PRICE_DECIMAL_PLACES,
        default=ProductCfg.PRICE_DEFAULT,
        verbose_name=ProductCfg.PRICE_VERBOSE_NAME,
        help_text=ProductCfg.PRICE_HELP_TEXT,
    )
    image = models.ImageField(
        upload_to=ProductCfg.IMAGE_UPLOAD_FOLDER,
        verbose_name=ProductCfg.IMAGE_VERBOSE_NAME,
        help_text=ProductCfg.IMAGE_HELP_TEXT,
    )
    thumbnail = ImageSpecField(
        source=ProductCfg.THUMBNAIL_SOURCE,
        processors=[
            ResizeToFill(
                ProductCfg.THUMBNAIL_PROCESSORS_WIDTH,
                ProductCfg.THUMBNAIL_PROCESSORS_HEIGHT,
            )
        ],
        format=ProductCfg.THUMBNAIL_FORMAT,
        options=ProductCfg.THUMBNAIL_OPTIONS,
    )
    preview = ImageSpecField(
        source=ProductCfg.PREVIEW_SOURCE,
        processors=[
            ResizeToFill(
                ProductCfg.PREVIEW_PROCESSORS_WIDTH,
                ProductCfg.PREVIEW_PROCESSORS_HEIGHT,
            )
        ],
        format=ProductCfg.PREVIEW_FORMAT,
        options=ProductCfg.PREVIEW_OPTIONS,
    )

    class Meta:
        """Мета-класс для модели продуктов."""

        verbose_name = ProductCfg.VERBOSE_NAME
        verbose_name_plural = ProductCfg.VERBOSE_NAME_PLURAL

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.title
