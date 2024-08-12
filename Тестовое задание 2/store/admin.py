"""Настройки админ-панелей для приложения Store."""

from django.contrib import admin
from store.models import Product, ProductCategory, ProductSubCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели ProductCategory.

    Настраивает отображение, поиск и автоматическое заполнение поля slug.
    """

    list_display = ("title", "slug", "description")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели ProductSubCategory.

    Настраивает отображение, поиск, фильтрацию и автоматическое заполнение
    поля slug.
    """

    list_display = ("title", "slug", "description", "product_category")
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
        "product_category",
        "product_subcategory",
        "price",
    )
    search_fields = ("title", "description")
    list_filter = ("product_category", "product_subcategory")
    prepopulated_fields = {"slug": ("title",)}
