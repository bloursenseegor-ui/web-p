from django.contrib import admin

from .models import Application, Review


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    """Настройка отображения заявок в стандартной панели Django Admin."""

    # Столбцы в списке записей
    list_display = ['user', 'course_name', 'start_date', 'payment', 'status', 'created_at']
    # Фильтры в боковой панели
    list_filter = ['status', 'payment']
    # Поиск по логину пользователя и названию курса
    search_fields = ['user__username', 'course_name']
    # Редактирование статуса прямо в списке без открытия записи
    list_editable = ['status']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Настройка отображения отзывов в стандартной панели Django Admin."""

    list_display = ['application', 'created_at']
