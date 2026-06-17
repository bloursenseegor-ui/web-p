# web-project — Портал записи на курсы

Django-сайт с регистрацией, подачей заявок и панелью администратора.

## Запуск (Windows)

```powershell
pip install django
python manage.py migrate
python manage.py runserver
```

Открыть в браузере: **http://localhost:8000**

Администратор создаётся автоматически при `migrate`.

## Что поменять под новую тему

### 1. apps.py — логин и пароль администратора
```python
User.objects.create_user(username='ЛОГИН', password='ПАРОЛЬ')
```

### 2. models.py — поля таблицы
```python
ПОЛЕ_1 = models.CharField(max_length=255)   # текстовое поле
ПОЛЕ_2 = models.DateField()                  # поле с датой
ПОЛЕ_3 = models.CharField(choices=...)       # поле с выбором
```
Также поменять варианты в `CHOICES` и тексты в `STATUS_CHOICES`.

### 3. views.py — названия полей в функции apply()
```python
ПОЛЕ_1 = request.POST.get('ПОЛЕ_1', '').strip()
Application.objects.create(ПОЛЕ_1=ПОЛЕ_1, ...)
```
Также поменять `'ЛОГИН_АДМИНА'` на логин из задания.

### 4. base.html — название сайта
```html
<title>НАЗВАНИЕ САЙТА</title>
🎓 НАЗВАНИЕ САЙТА
```

### 5. apply.html — поля формы
- Подписи полей (`<label>`)
- Атрибуты `name=""` у полей (должны совпадать с views.py)
- Варианты в `<select>` и `<input type="radio">`

### 6. applications.html — карточка заявки
```html
{{ app.ПОЛЕ_1 }}
{{ app.ПОЛЕ_2 }}
{{ app.get_ПОЛЕ_3_display }}
```

### 7. admin_panel.html — таблица заявок
- Названия столбцов `<th>`
- Поля в строках `{{ app.ПОЛЕ_1 }}`
- Варианты статусов в `<select>`

## После изменения models.py — обязательно!
```powershell
python manage.py makemigrations
python manage.py migrate
```

## Если что-то сломалось — сброс базы
```powershell
del db.sqlite3
python manage.py migrate
```

## Страницы

| Адрес | Страница |
|-------|----------|
| /login/ | Вход |
| /register/ | Регистрация |
| /applications/ | Мои заявки |
| /apply/ | Новая заявка |
| /admin-panel/ | Панель администратора |

## Структура файлов

```
web-p/
├── manage.py
├── config/
│   ├── settings.py
│   └── urls.py
└── main/
    ├── models.py      ← поля таблицы
    ├── views.py       ← логика страниц
    ├── urls.py        ← адреса страниц
    ├── apps.py        ← создание админа
    ├── templates/
    │   ├── base.html          ← название сайта
    │   ├── apply.html         ← форма заявки
    │   ├── applications.html  ← список заявок
    │   └── admin_panel.html   ← панель админа
    └── static/
        └── css/style.css
```
