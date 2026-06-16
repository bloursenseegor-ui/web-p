#!/usr/bin/env python
"""
Утилита командной строки Django.
Этот файл НЕ ТРОГАТЬ — он одинаковый для любого проекта.
"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Django не установлен. Выполни: pip3 install django'
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
