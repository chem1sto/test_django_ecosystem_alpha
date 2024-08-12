"""Приложение store."""
from django.apps import AppConfig


class StoreConfig(AppConfig):
    """Базовая конфигурация для приложения store."""
    default_auto_field = "django.db.models.BigAutoField"
    name = "store"
    verbose = "Магазин продуктов"
