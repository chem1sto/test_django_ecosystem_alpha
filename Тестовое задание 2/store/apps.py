"""Приложение store."""

from django.apps import AppConfig


class StoreConfig(AppConfig):
    """Базовая конфигурация для приложения store."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "store"
    verbose_name = "Магазин продуктов"

    def ready(self):
        """
        Импортирует сигналы при готовности приложения.

        Этот метод вызывается, когда приложение Django готово к использованию.
        """
        import store.signals
