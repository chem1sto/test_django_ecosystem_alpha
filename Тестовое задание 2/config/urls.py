"""
Конфигурация URL-адресов для проекта test_django_ecosystem_alpha.

URL-адреса:
- `admin/`: Административная панель Django.
- `api/`: API-endpoints.
- `swagger<format>/`: JSON-документация API.
- `swagger/`: Интерфейс Swagger UI для документации API.
- `redoc/`: Интерфейс Redoc для документации API.

Список `urlpatterns` направляет URL-адреса в соответствующие представления.
Дополнительная информация об этом файле доступна по ссылке
    https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Django Ecosystem Alpha",
        default_version="v1",
        description=(
            "Документация для приложений проекта django_ecosystem_alpha"
        ),
        contact=openapi.Contact(email="admin@mymail.ru"),
        license=openapi.License(name="MIT license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

if settings.DEBUG:
    """
    В режиме отладки добавляем URL-адреса для обслуживания медиа-файлов.
    Это позволяет просматривать загруженные медиа-файлы непосредственно в
    браузере.
    """
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
