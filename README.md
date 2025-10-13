# FirstDjango_11102025

## Инструкция по развертыванию проекта
1. Создать виртуальное окружение
```
python3 -m venv django_venv
```

2. Активировать вирутальное окружение
```
source django_venv/bin/activate
```

3. Установить нужные библиотеки в виртуальное окружение
```
pip install -r requirements.txt
```

4. Запуск сервера
```
python manage.py runserver
```

## Дополнительно
1. Полезные расширения для шаблонов: `django`
```
ext install batisteo.vscode-django
```
2. Добавить в `settings.json`:
```
"emmet.includeLanguages": {
        "django-html": "html"
    },
    "files.associations": {
        "*.html": "django-html"
    }
```