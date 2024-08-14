"""Константы и настройки для моделей проекта."""
REQUEST = "request"


class AdminStoreCfg:
    """Настройки для админ-панели Магазина Продуктов."""

    IMAGE_THUMBNAIL_FORMAT_STRING = "<img src='{}' width='40' height='40' />"
    IMAGE_THUMBNAIL_NO_IMAGE = "Нет изображения"
    IMAGE_THUMBNAIL_SHORT_DESCRIPTION = "Миниатюра"
    PRODUCT_CATEGORY_ADMIN_LIST_DISPLAY = (
        "title",
        "slug",
        "description",
        "image_thumbnail",
    )
    PRODUCT_CATEGORY_ADMIN_SEARCH_FIELDS = ("title",)
    PRODUCT_CATEGORY_ADMIN_PREPOPULATED_FIELDS = {"slug": ("title",)}
    PRODUCT_SUBCATEGORY_ADMIN_LIST_DISPLAY = (
        "title",
        "slug",
        "description",
        "product_category",
        "image_thumbnail",
    )
    PRODUCT_SUBCATEGORY_ADMIN_SEARCH_FIELDS = ("title", "description")
    PRODUCT_SUBCATEGORY_ADMIN_LIST_FILTER = ("product_category",)
    PRODUCT_SUBCATEGORY_ADMIN_PREPOPULATED_FIELDS = {"slug": ("title",)}
    PRODUCT_ADMIN_LIST_DISPLAY = (
        "title",
        "slug",
        "description",
        "product_category",
        "product_subcategory",
        "price_with_currency",
        "image_thumbnail",
    )
    PRODUCT_ADMIN_SEARCH_FIELDS = ("title", "description")
    PRODUCT_ADMIN_LIST_FILTER = ("product_category", "product_subcategory")
    PRODUCT_ADMIN_PREPOPULATED_FIELDS = {"slug": ("title",)}
    PRODUCT_PRICE_WITH_CURRENCY = "{price} руб."
    PRODUCT_NO_PRICE = "Нет цены"
    PRODUCT_PRICE_WITH_CURRENCY_SHORT_DESCRIPTION = "Стоимость"
    PRODUCT_IMAGE_THUMBNAIL_FORMAT_STRING = (
        "<img src='{}' width='40' height='40' />"
    )


class BaseProductCategoryCfg:
    """Настройки для абстрактной модели BaseProductCategory."""

    TITLE_MAX_LENGTH = 255
    TITLE_VERBOSE_NAME = "Наименование категории продукта"
    TITLE_HELP_TEXT = "Введите наименование категории продукта"
    SLUG_MAX_LENGTH = 100
    SLUG_HELP_TEXT = (
        "Введите уникальное название для категории (подкатегории) продуктов "
        "(по умолчанию генерируется slug на основе наименования)"
    )
    DESCRIPTION_MAX_LENGTH = 5000
    DESCRIPTION_VERBOSE_NAME = "Описание категории продукта"
    DESCRIPTION_HELP_TEXT = (
        f"Введите описание товара до {DESCRIPTION_MAX_LENGTH} символов"
    )
    IMAGE_UPLOAD_FOLDER = "products_categories/"
    IMAGE_VERBOSE_NAME = "Изображение для категории продуктов"
    IMAGE_HELP_TEXT = "Загрузите изображение для категории продукта"


class CartCfg:
    """Настройки для модели Cart."""

    CART_STR = "Корзина пользователя {username}"


class CartItemCfg:
    """Настройки для модели CartItem."""

    CART_ITEM_STR = "{quantity} x {product} in {cart}"
    CART_ITEM_RELATED_NAME = "items"
    CART_ITEM_DEFAULT_QUANTITY = 0


class ProductCfg:
    """Настройки для модели Product."""

    VERBOSE_NAME = "продукт"
    VERBOSE_NAME_PLURAL = "продукты"
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
    PRICE_VERBOSE_NAME = "Стоимость продукта"
    PRICE_HELP_TEXT = "Введите стоимость продукта"
    IMAGE_UPLOAD_FOLDER = "products/"
    IMAGE_VERBOSE_NAME = "Изображение для продукта"
    IMAGE_HELP_TEXT = "Выберите изображение для продукта"
    THUMBNAIL_SOURCE = PREVIEW_SOURCE = "image"
    THUMBNAIL_PROCESSORS_WIDTH = 100
    THUMBNAIL_PROCESSORS_HEIGHT = 100
    THUMBNAIL_FORMAT = PREVIEW_FORMAT = "PNG"
    THUMBNAIL_OPTIONS = {"quality": 60}
    PREVIEW_PROCESSORS_WIDTH = 400
    PREVIEW_PROCESSORS_HEIGHT = 400
    PREVIEW_OPTIONS = {"quality": 75}


class ProductCategoryCfg:
    """Настройки для модели Product."""

    PRODUCT_CATEGORY_ORDER = ["title"]
    VERBOSE_NAME = "категория продуктов"
    VERBOSE_NAME_PLURAL = "категории продуктов"


class ProductSubCategoryCfg:
    """Настройки для модели ProductSubCategory."""

    VERBOSE_NAME = "подкатегория продуктов"
    VERBOSE_NAME_PLURAL = "подкатегории продуктов"
    TITLE_MAX_LENGTH = 255
    TITLE_VERBOSE_NAME = "Наименование подкатегории продукта"
    TITLE_HELP_TEXT = "Введите наименование подкатегории продукта"
    DESCRIPTION_MAX_LENGTH = 5000
    DESCRIPTION_VERBOSE_NAME = "Описание подкатегории продукта"
    DESCRIPTION_HELP_TEXT = (
        f"Введите описание продукта до {DESCRIPTION_MAX_LENGTH} символов"
    )
    IMAGE_UPLOAD_FOLDER = "products_subcategories/"
    IMAGE_VERBOSE_NAME = "Изображение для подкатегории продуктов"
    IMAGE_HELP_TEXT = "Загрузите изображение для подкатегории продуктов"
    PRODUCT_CATEGORY_RELATED_NAME = "subcategories"
    PRODUCT_CATEGORY_VERBOSE_NAME = "Категория продукта"
    PRODUCT_CATEGORY_HELP_TEXT = "Выберите категорию продукта"


class SerializersCfg:
    """Настройки для сериалайзеров приложения api."""

    PRODUCT_TITLE = "product.title"
    QUANTITY_DEFAULT = 1
    PRODUCT_SUBCATEGORY_SERIALIZER_META_FIELDS = ("title", "slug")
    PRODUCT_CATEGORY_SERIALIZER_META_FIELDS = (
        "title",
        "slug",
        "subcategories",
    )
    PRODUCT_SERIALIZER_META_FIELDS = (
        "title",
        "slug",
        "product_category",
        "product_subcategory",
        "price",
        "images",
    )
    CART_ITEM_SERIALIZER_META_FIELDS = ("product", "quantity")
    SHORT_CART_ITEM_SERIALIZER_META_FIELDS = ("product",)
    CART_SERIALIZER_META_FIELDS = (
        "user",
        "items",
        "total_quantity",
        "total_price",
    )


class ViewsCfg:
    """Настройки для представлений приложения api."""

    ADD_ITEM_HTTP_METHODS = ("post",)
    REMOVE_ITEM_HTTP_METHODS = ("delete",)
    UPDATE_ITEM_HTTP_METHODS = ("patch",)
    CLEAR_CART_HTTP_METHODS = ("delete",)
    PRODUCT = "product"
    QUANTITY = "quantity"
    QUANTITY_DEFAULT_VALUE = 1
    GET_PRODUCT_VALIDATION_ERROR = (
        "Продукта с наименованием {product_title} не существует."
    )
    CART_ITEM_VALIDATION_ERROR = "Элемент корзины {product} не существует."
