"""Приложение api."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Базовая конфигурация для приложения api."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
