"""Настройки админ-панелей для приложения Store."""

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
                "<img src='{}' width='40' height='40' />", obj.image.url
            )
        return "Нет изображения"

    image_thumbnail.short_description = "Миниатюра"


@admin.register(ProductCategory)
class ProductCategoryAdmin(ImageThumbnailMixin, admin.ModelAdmin):
    """
    Админ-панель для модели ProductCategory.

    Настраивает отображение, поиск и автоматическое заполнение поля slug.
    """

    list_display = ("title", "slug", "description", "image_thumbnail")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(ImageThumbnailMixin, admin.ModelAdmin):
    """
    Админ-панель для модели ProductSubCategory.

    Настраивает отображение, поиск, фильтрацию и автоматическое заполнение
    поля slug.
    """

    list_display = (
        "title",
        "slug",
        "description",
        "product_category",
        "image_thumbnail",
    )
    search_fields = ("title", "description")
    list_filter = ("product_category",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Product.

    Настраивает отображение, поиск, фильтрацию и автоматическое заполнение
    поля slug.
    """

    list_display = (
        "title",
        "slug",
        "description",
        "product_category",
        "product_subcategory",
        "price_with_currency",
        "image_thumbnail",
    )
    search_fields = ("title", "description")
    list_filter = ("product_category", "product_subcategory")
    prepopulated_fields = {"slug": ("title",)}

    def price_with_currency(self, obj):
        """Выводит стоимость продукта с указанием валюты в админ-панель."""
        if obj.price:
            return "{} руб.".format(localize(obj.price))
        return "Нет цены"

    price_with_currency.short_description = "Стоимость"

    def image_thumbnail(self, obj):
        """Выводит миниатюру подкатегории товара в админ-панель."""
        if obj.thumbnail:
            return format_html(
                "<img src='{}' width='40' height='40' />", obj.thumbnail.url
            )
        return "Нет изображения"

    image_thumbnail.short_description = "Миниатюра"
