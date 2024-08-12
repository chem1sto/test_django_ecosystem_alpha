# Django экосистема Альфа
## Тестовое задание на позицию стажёра "Python Backend разработчик"

## О проекте
&ensp; &nbsp; В данном проекте представлено две папки "Тестовое задание 1" и 
"Тестовое задание 2". В них находятся решения соответственно задания 1 и 
задания 2.

### Тестовое задание 1:
Напишите программу, которая выводит n первых элементов последовательности 
122333444455555… (число повторяется столько раз, чему оно равно).

### Тестовое задание 2:
Реализовать Django проект магазина продуктов со следующим функционалом:
- Должна быть реализована возможность создания, редактирования, удаления 
категорий и подкатегорий товаров в админке;
- Категории и подкатегории обязательно должны иметь наименование, slug-имя, 
изображение;
- Подкатегории должны быть связаны с родительской категорией;
- Должен быть реализован эндпоинт для просмотра всех категорий с 
подкатегориями. Должны быть предусмотрена пагинация;
- Должна быть реализована возможность добавления, изменения, удаления 
продуктов в админке;
- Продукты должны относится к определенной подкатегории и, соответственно 
категории, должны иметь наименование, slug-имя, изображение в 3-х размерах, 
цену;
- Должен быть реализован эндпоинт вывода продуктов с пагинацией. Каждый 
продукт в выводе должен иметь поля: наименование, slug, категория, 
подкатегория, цена, список изображений;
- Реализовать эндпоинт добавления, изменения (изменение количества), удаления 
продукта в корзине;
- Реализовать эндпоинт вывода состава корзины с подсчетом количества товаров и 
суммы стоимости товаров в корзине;
- Реализовать возможность полной очистки корзины;
- Операции по эндпоинтам категорий и продуктов может осуществлять любой 
пользователь;
- Операции по эндпоинтам корзины может осуществлять только авторизированный 
пользователь и только со своей корзиной;
- Реализовать авторизацию по токену.

## Технологии
- Python
- Django
- Django Rest Framework
- Djoser
- Simple JWT
- drf-yasg

## Как запустить проект Django из тестового задания 2

### Запуск проекта в dev-режиме
1. Клонировать репозиторий и перейти в него в командной строке:
    ```bash
    git clone git@github.com:chem1sto/test_django_ecosystem_alpha.git
    ```
2. Создать и активировать виртуальное окружение:
    ```bash
    cd ./test_django_ecosystem_alpha/ &&
    python3 -m venv venv
    ```
    * Для Linux/macOS
    ```bash
    source venv/bin/activate
    ```
    * Для Windows
    ```shell
    source venv/scripts/activate
    ```
3. Установить зависимости из файла requirements.txt:
   ```
   python3 -m pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. Создайте переменные окружения в основной папке проекта
    ```bash
    touch .env
    ```
5. Добавьте ваши данные в файл .env (подробнее в .env.example)
    ```
    SECRET_KEY="Секретный код Django"
    DEBUG="True или False"
    ALLOWED_HOSTS="IP (домен) вашего сервера"
    ```
6. Для запуска проекта перейдите в папку с файлом manage.py и выполните команды:
   ```bash
   cd ../test_django_ecosystem_alpha/Тестовое задание 2/src/ &&
   python manage.py makemigrations &&
   python manage.py migrate &&
   python manage.py collectstatic --noinput
   python manage.py runserver
   ```

## Автор
[Васильев Владимир](https://github.com/chem1sto)

## Лицензия
Пожалуйста, ознакомьтесь с [MIT license](https://github.com/chem1sto/test_django_ecosystem_alpha?tab=MIT-1-ov-file)
