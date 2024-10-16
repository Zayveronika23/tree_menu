# Tree_menu - приложение, которое создает древовидное меню.           


### Краткое описание:
Приложение, разработанное на основе фреймворка Django, которое позволяет отрисовать древовидное меню на любой странице с помощью тега {% draw_menu 'Название меню' %}. Вносить меню в БД и редактировать его можно через админ-панель. Для максимально эффективного выполнения операций использован модуль django-mptt.

### Стек технологий:
    Python
    Django REST Framework

### Сборка и запуск:

```bash
Клонируем репозиторий
git clone git@github.com:<nickname>/tree_menu.git

Переходим в директорию
cd tree_menu

Создаем и активируем виртуальное окружение
python3 -m venv venv
source venv/bin/activate

Устанавливаем зависимости
pip install -r requirements.txt

Переходим в директорию
cd tree_menu/

Создаем и применяем миграции
python manage.py makemigrations
python manage.py migrate

Создаем администратора
python manage.py createsuperuser

Запускаем проект
python manage.py runserver
```
Далее рекомендуется создать меню в панели администратора и прописать название меню в теге  {% draw_menu 'Название меню' %}.
