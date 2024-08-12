"""Модуль для определения моделей приложения store."""

from core.constants import (
    BaseProductCategoryCfg,
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
        allow_unicode=True,
        unique=True,
    )
    description = models.TextField(
        max_length=BaseProductCategoryCfg.DESCRIPTION_MAX_LENGTH,
        verbose_name=BaseProductCategoryCfg.DESCRIPTION_VERBOSE_NAME,
        help_text=BaseProductCategoryCfg.DESCRIPTION_HELP_TEXT,
    )
    image = models.ImageField(
        upload_to=BaseProductCategoryCfg.IMAGE_UPLOAD_FOLDER,
    )

    class Meta:
        """Мета-класс для абстрактной базовой модели."""

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
    )
    product_category = models.ForeignKey(
        to=ProductCategory,
        on_delete=models.CASCADE,
        verbose_name=ProductSubCategoryCfg.PRODUCT_CATEGORY_VERBOSE_NAME,
        help_text=ProductSubCategoryCfg.PRODUCT_CATEGORY_HELP_TEXT,
    )


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
    )
    image = models.ImageField(
        upload_to=ProductCfg.IMAGE_UPLOAD_FOLDER,
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

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return self.title
