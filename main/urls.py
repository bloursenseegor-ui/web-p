from django.urls import path

from . import views

urlpatterns = [
    # Главная страница — перенаправляет в зависимости от авторизации
    path('', views.index, name='index'),
    # Регистрация нового пользователя
    path('register/', views.register, name='register'),
    # Вход в систему
    path('login/', views.login_view, name='login'),
    # Выход из системы
    path('logout/', views.logout_view, name='logout'),
    # Список заявок текущего пользователя
    path('applications/', views.applications, name='applications'),
    # Форма создания новой заявки
    path('apply/', views.apply, name='apply'),
    # Панель администратора (только для пользователя Admin)
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    # Изменение статуса заявки по её идентификатору
    path('change-status/<int:pk>/', views.change_status, name='change_status'),
]
