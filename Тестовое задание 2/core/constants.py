"""Константы и настройки для моделей проекта."""


class BaseProductCategoryCfg:
    """Настройки для абстрактной модели BaseProductCategory."""

    TITLE_MAX_LENGTH = 255
    TITLE_VERBOSE_NAME = "Наименование категории продукта"
    TITLE_HELP_TEXT = "Введите наименование категории продукта"
    SLUG_MAX_LENGTH = 100
    DESCRIPTION_MAX_LENGTH = 5000
    DESCRIPTION_VERBOSE_NAME = "Описание категории продукта"
    DESCRIPTION_HELP_TEXT = (
        f"Введите описание товара до {DESCRIPTION_MAX_LENGTH} символов"
    )
    IMAGE_UPLOAD_FOLDER = "products_categories/"


class ProductSubCategoryCfg:
    """Настройки для модели ProductSubCategory."""

    TITLE_MAX_LENGTH = 255
    TITLE_VERBOSE_NAME = "Наименование подкатегории продукта"
    TITLE_HELP_TEXT = "Введите наименование подкатегории продукта"
    DESCRIPTION_MAX_LENGTH = 5000
    DESCRIPTION_VERBOSE_NAME = "Описание подкатегории продукта"
    DESCRIPTION_HELP_TEXT = (
        f"Введите описание продукта до {DESCRIPTION_MAX_LENGTH} символов"
    )
    IMAGE_UPLOAD_FOLDER = "products_subcategories/"
    PRODUCT_CATEGORY_VERBOSE_NAME = "Категория продукта для его подкатегории"
    PRODUCT_CATEGORY_HELP_TEXT = (
        "Выберите категорию продукта для его подкатегории"
    )


class ProductCfg:
    """Настройки для модели Product."""

    TITLE_MAX_LENGTH = 255
    TITLE_VERBOSE_NAME = "Наименование продукта"
    TITLE_HELP_TEXT = "Введите наименование продукта"
    SLUG_MAX_LENGTH = 100
    DESCRIPTION_MAX_LENGTH = 5000
    DESCRIPTION_VERBOSE_NAME = "Описание продукта"
    DESCRIPTION_HELP_TEXT = (
        f"Введите описание продукта до {DESCRIPTION_MAX_LENGTH} символов"
    )
    PRODUCT_CATEGORY_RELATED_NAME = "product_category"
    PRODUCT_CATEGORY_VERBOSE_NAME = "Категория продукта"
    PRODUCT_CATEGORY_HELP_TEXT = "Выберите категорию продукта"
    PRODUCT_SUBCATEGORY_RELATED_NAME = "product_subcategory"
    PRODUCT_SUBCATEGORY_VERBOSE_NAME = "Подкатегория продукта"
    PRODUCT_SUBCATEGORY_HELP_TEXT = "Выберите подкатегорию продукта"
    PRICE_MAX_DIGITS = 10
    PRICE_DECIMAL_PLACES = 2
    PRICE_DEFAULT = 0.00
    IMAGE_UPLOAD_FOLDER = "products/"
    THUMBNAIL_SOURCE = PREVIEW_SOURCE = "image"
    THUMBNAIL_PROCESSORS_WIDTH = 100
    THUMBNAIL_PROCESSORS_HEIGHT = 100
    THUMBNAIL_FORMAT = PREVIEW_FORMAT = "PNG"
    THUMBNAIL_OPTIONS = {"quality": 60}
    PREVIEW_PROCESSORS_WIDTH = 400
    PREVIEW_PROCESSORS_HEIGHT = 400
    PREVIEW_OPTIONS = {"quality": 75}
