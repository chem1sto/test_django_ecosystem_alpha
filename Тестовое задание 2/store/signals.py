"""Модуль для обработки сигналов приложения store."""

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from store.models import BaseProductCategory, Product


@receiver(pre_save, sender=BaseProductCategory)
@receiver(pre_save, sender=Product)
def generate_slug(sender, instance, **kwargs):
    """
    Генерирует slug для модели, если он не задан.

    Этот сигнал вызывается перед сохранением экземпляра модели.
    Если поле slug не заполнено, оно будет сгенерировано на основе поля title.

    Параметры:
        sender: Класс модели, отправляющий сигнал.
        instance: Экземпляр модели, который будет сохранен.
        **kwargs: Дополнительные аргументы.
    """
    if not instance.slug:
        instance.slug = slugify(instance.title)
