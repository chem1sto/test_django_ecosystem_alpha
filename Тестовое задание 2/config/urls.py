"""
Конфигурация URL-адресов для проекта test_django_ecosystem_alpha.

URL-адреса:
- `admin/`: Административная панель Django.

Список `urlpatterns` направляет URL-адреса в представления.
Дополнительная информация об этом файле доступна по ссылке
    https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
