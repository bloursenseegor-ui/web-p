# web-project — Портал записи на курсы

Django-сайт с регистрацией, подачей заявок и панелью администратора.

## Запуск

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Открыть: **http://localhost:8000**

Администратор создаётся автоматически при `migrate`:
- Логин: `Admin`
- Пароль: `KorokNET`

## Страницы

| Адрес | Страница |
|-------|----------|
| /login/ | Вход |
| /register/ | Регистрация |
| /applications/ | Мои заявки |
| /apply/ | Новая заявка |
| /admin-panel/ | Панель администратора |

## Структура

```
web-project/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── main/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── apps.py
    ├── admin.py
    ├── templates/
    └── static/
```
