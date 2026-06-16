from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Стандартная панель Django Admin для управления данными
    path('django-admin/', admin.site.urls),
    # Все пользовательские маршруты подключаются из main/urls.py
    path('', include('main.urls')),
]
