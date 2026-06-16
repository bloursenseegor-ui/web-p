from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    """Заявка на обучение, связанная с пользователем."""

    # Варианты способа оплаты
    PAYMENT_CHOICES = [
        ('cash', 'Наличными'),
        ('transfer', 'Переводом по номеру телефона'),
    ]

    # Варианты статуса заявки
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('learning', 'Идет обучение'),
        ('done', 'Обучение завершено'),
    ]

    # Связь с пользователем: при удалении пользователя удаляются все его заявки
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    # Название курса — строка до 255 символов
    course_name = models.CharField(
        max_length=255,
        verbose_name='Название курса'
    )

    # Желаемая дата начала обучения
    start_date = models.DateField(
        verbose_name='Дата начала'
    )

    # Способ оплаты — выбор из PAYMENT_CHOICES
    payment = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES,
        verbose_name='Способ оплаты'
    )

    # Статус заявки — по умолчанию «Новая»
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
        return f'{self.user.username} — {self.course_name}'


class Review(models.Model):
    """Отзыв об обучении, привязанный к конкретной заявке (один к одному)."""

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
