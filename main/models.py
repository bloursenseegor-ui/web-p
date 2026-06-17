from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    """Заявка пользователя, связанная с его аккаунтом."""

    # Варианты для выпадающего списка или radio-кнопок (ПОЛЕ_3)
    ПОЛЕ_3_CHOICES = [
        ('ВАРИАНТ_1_КОД', 'ВАРИАНТ_1_ТЕКСТ'),
        ('ВАРИАНТ_2_КОД', 'ВАРИАНТ_2_ТЕКСТ'),
    ]

    # Варианты статуса заявки
    STATUS_CHOICES = [
        ('new', 'СТАТУС_1'),
        ('active', 'СТАТУС_2'),
        ('done', 'СТАТУС_3'),
    ]

    # Связь с пользователем: при удалении пользователя удаляются все его заявки
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    # Текстовое поле — строка до 255 символов
    ПОЛЕ_1 = models.CharField(
        max_length=255,
        verbose_name='НАЗВАНИЕ_ПОЛЯ_1'
    )

    # Поле с датой
    ПОЛЕ_2 = models.DateField(
        verbose_name='НАЗВАНИЕ_ПОЛЯ_2'
    )

    # Поле с выбором из списка
    ПОЛЕ_3 = models.CharField(
        max_length=20,
        choices=ПОЛЕ_3_CHOICES,
        verbose_name='НАЗВАНИЕ_ПОЛЯ_3'
    )

    # Статус заявки — по умолчанию первый статус
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )

    # Дата создания заявки — заполняется автоматически
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']  # новые заявки отображаются первыми

    def __str__(self):
        return f'{self.user.username} — {self.ПОЛЕ_1}'


class Review(models.Model):
    """Отзыв, привязанный к конкретной заявке (один к одному)."""

    # Связь с заявкой: один отзыв на одну заявку
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        verbose_name='Заявка',
        related_name='review'
    )

    # Текст отзыва
    text = models.TextField(verbose_name='Текст отзыва')

    # Дата написания отзыва — заполняется автоматически
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата отзыва'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв на заявку #{self.application.id}'
