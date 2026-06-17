from django.apps import AppConfig


def create_admin(sender, **kwargs):
    """Создаёт администратора автоматически после применения миграций."""
    from django.contrib.auth.models import User
    if not User.objects.filter(username='ЛОГИН_АДМИНА').exists():
        User.objects.create_user(username='ЛОГИН_АДМИНА', password='ПАРОЛЬ_АДМИНА')


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        # Подключаем сигнал post_migrate для автосоздания администратора
        from django.db.models.signals import post_migrate
        post_migrate.connect(create_admin, sender=self)
