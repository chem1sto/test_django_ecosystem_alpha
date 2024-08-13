"""Настройки админ-панелей для приложения Store."""

from core.constants import AdminStoreCfg
from django.contrib import admin
from django.utils.formats import localize
from django.utils.html import format_html
from store.models import Product, ProductCategory, ProductSubCategory


class ImageThumbnailMixin:
    """Миксин для вывода миниатюр изображений в админ-панели."""

    def image_thumbnail(self, obj):
        """Выводит миниатюру изображения в админ-панель."""
        if obj.image:
            return format_html(
                AdminStoreCfg.IMAGE_THUMBNAIL_FORMAT_STRING, obj.image.url
            )
        return AdminStoreCfg.IMAGE_THUMBNAIL_NO_IMAGE

    image_thumbnail.short_description = (
        AdminStoreCfg.IMAGE_THUMBNAIL_SHORT_DESCRIPTION
    )


@admin.register(ProductCategory)
class ProductCategoryAdmin(ImageThumbnailMixin, admin.ModelAdmin):
    """
    Админ-панель для модели ProductCategory.

    Настраивает отображение, поиск и автоматическое заполнение поля slug.
    """

    list_display = AdminStoreCfg.PRODUCT_CATEGORY_ADMIN_LIST_DISPLAY
    search_fields = AdminStoreCfg.PRODUCT_CATEGORY_ADMIN_SEARCH_FIELDS
    prepopulated_fields = (
        AdminStoreCfg.PRODUCT_CATEGORY_ADMIN_PREPOPULATED_FIELDS
    )


@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(ImageThumbnailMixin, admin.ModelAdmin):
    """
    Админ-панель для модели ProductSubCategory.

    Настраивает отображение, поиск, фильтрацию и автоматическое заполнение
    поля slug.
    """

    list_display = AdminStoreCfg.PRODUCT_SUBCATEGORY_ADMIN_LIST_DISPLAY
    search_fields = AdminStoreCfg.PRODUCT_SUBCATEGORY_ADMIN_SEARCH_FIELDS
    list_filter = AdminStoreCfg.PRODUCT_SUBCATEGORY_ADMIN_LIST_FILTER
    prepopulated_fields = (
        AdminStoreCfg.PRODUCT_SUBCATEGORY_ADMIN_PREPOPULATED_FIELDS
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Product.

    Настраивает отображение, поиск, фильтрацию и автоматическое заполнение
    поля slug.
    """

    list_display = AdminStoreCfg.PRODUCT_ADMIN_LIST_DISPLAY
    search_fields = AdminStoreCfg.PRODUCT_ADMIN_SEARCH_FIELDS
    list_filter = AdminStoreCfg.PRODUCT_ADMIN_LIST_FILTER
    prepopulated_fields = AdminStoreCfg.PRODUCT_ADMIN_PREPOPULATED_FIELDS

    def price_with_currency(self, obj):
        """Выводит стоимость продукта с указанием валюты в админ-панель."""
        if obj.price:
            return AdminStoreCfg.PRODUCT_PRICE_WITH_CURRENCY.format(
                price=localize(obj.price)
            )
        return AdminStoreCfg.PRODUCT_NO_PRICE

    price_with_currency.short_description = (
        AdminStoreCfg.PRODUCT_PRICE_WITH_CURRENCY_SHORT_DESCRIPTION
    )

    def image_thumbnail(self, obj):
        """Выводит миниатюру подкатегории товара в админ-панель."""
        if obj.thumbnail:
            return format_html(
                AdminStoreCfg.IMAGE_THUMBNAIL_FORMAT_STRING, obj.thumbnail.url
            )
        return AdminStoreCfg.IMAGE_THUMBNAIL_NO_IMAGE

    image_thumbnail.short_description = (
        AdminStoreCfg.IMAGE_THUMBNAIL_SHORT_DESCRIPTION
    )
