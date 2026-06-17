import re

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .models import Application, Review


def index(request):
    """Главная страница — перенаправляет в зависимости от авторизации."""
    if request.user.is_authenticated:
        return redirect('applications')
    return redirect('login')


def register(request):
    """Регистрация нового пользователя с валидацией полей формы."""
    errors = {}

    if request.method == 'POST':
        # Получаем данные из формы и убираем пробелы по краям
        login_val = request.POST.get('login', '').strip()
        password = request.POST.get('password', '').strip()
        fio = request.POST.get('fio', '').strip()
        phone = request.POST.get('phone', '').strip()
        email = request.POST.get('email', '').strip()

        # Логин: только латиница и цифры, минимум 6 символов
        if not re.match(r'^[a-zA-Z0-9]{6,}$', login_val):
            errors['login'] = 'Только латиница и цифры, минимум 6 символов'
        elif User.objects.filter(username=login_val).exists():
            errors['login'] = 'Такой логин уже занят'

        # Пароль: минимум 8 символов
        if len(password) < 8:
            errors['password'] = 'Минимум 8 символов'

        # ФИО: только кириллица и пробелы
        if not re.match(r'^[а-яА-ЯёЁ\s]+$', fio):
            errors['fio'] = 'Только кириллица и пробелы'

        # Телефон: формат 8(XXX)XXX-XX-XX
        if not re.match(r'^8\(\d{3}\)\d{3}-\d{2}-\d{2}$', phone):
            errors['phone'] = 'Формат: 8(XXX)XXX-XX-XX'

        # Email: должен содержать @ и домен
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            errors['email'] = 'Введите корректный email'

        if not errors:
            # create_user автоматически хэширует пароль перед сохранением
            User.objects.create_user(
                username=login_val,
                password=password,
                email=email,
                first_name=fio
            )
            return redirect('login')

    return render(request, 'register.html', {'errors': errors})


def login_view(request):
    """Вход в систему — проверяет логин и пароль, создаёт сессию."""
    error = ''

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # authenticate возвращает объект пользователя или None
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Администратора направляем в панель управления
            if username == 'ЛОГИН_АДМИНА':
                return redirect('admin_panel')
            return redirect('applications')
        else:
            error = 'Неверный логин или пароль'

    return render(request, 'login.html', {'error': error})


def logout_view(request):
    """Выход из системы — завершает сессию и перенаправляет на вход."""
    logout(request)
    return redirect('login')


@login_required
def applications(request):
    """Список заявок текущего пользователя. Позволяет оставить отзыв."""
    if request.method == 'POST':
        app_id = request.POST.get('app_id')
        review_text = request.POST.get('review_text', '').strip()

        # Проверяем, что заявка принадлежит текущему пользователю
        app = get_object_or_404(Application, id=app_id, user=request.user)

        # Отзыв можно оставить только если статус «завершено»
        if app.status == 'done' and review_text:
            # get_or_create — создаёт отзыв, если его ещё нет
            Review.objects.get_or_create(
                application=app,
                defaults={'text': review_text}
            )

    # Выбираем только заявки текущего пользователя
    user_applications = Application.objects.filter(user=request.user)
    return render(request, 'applications.html', {'applications': user_applications})


@login_required
def apply(request):
    """Создание новой заявки."""
    if request.method == 'POST':
        # Имена полей должны совпадать с атрибутом name в HTML-форме
        ПОЛЕ_1 = request.POST.get('ПОЛЕ_1', '').strip()
        ПОЛЕ_2 = request.POST.get('ПОЛЕ_2', '').strip()
        ПОЛЕ_3 = request.POST.get('ПОЛЕ_3', '').strip()

        # Сохраняем заявку в базу данных
        Application.objects.create(
            user=request.user,
            ПОЛЕ_1=ПОЛЕ_1,
            ПОЛЕ_2=ПОЛЕ_2,
            ПОЛЕ_3=ПОЛЕ_3,
        )
        return redirect('applications')

    return render(request, 'apply.html')


def admin_panel(request):
    """Панель администратора — доступна только пользователю ЛОГИН_АДМИНА."""
    if not request.user.is_authenticated or request.user.username != 'ЛОГИН_АДМИНА':
        return redirect('login')

    # Получаем все заявки всех пользователей
    all_applications = Application.objects.all()
    return render(request, 'admin_panel.html', {'applications': all_applications})


def change_status(request, pk):
    """Изменение статуса заявки администратором. pk — идентификатор заявки."""
    if not request.user.is_authenticated or request.user.username != 'ЛОГИН_АДМИНА':
        return redirect('login')

    if request.method == 'POST':
        app = get_object_or_404(Application, pk=pk)
        app.status = request.POST.get('status')
        app.save()

    return redirect('admin_panel')
