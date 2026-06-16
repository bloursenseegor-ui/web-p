from django.contrib.auth.models import User

ADMIN_LOGIN    = 'Admin'
ADMIN_PASSWORD = 'KorokNET'

if not User.objects.filter(username=ADMIN_LOGIN).exists():
    User.objects.create_user(username=ADMIN_LOGIN, password=ADMIN_PASSWORD)
    print(f'Администратор {ADMIN_LOGIN} создан.')
else:
    print(f'Администратор {ADMIN_LOGIN} уже существует.')
