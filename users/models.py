from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson, NULLABLE

FREQUENCY_CHOICES = (
    ('1', 'наличные'),
    ('2', 'перевод на счет'),
)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    citi = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    photo = models.ImageField(upload_to='users', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date_payment = models.DateField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE,
                               related_name='annotation_set')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE,
                               related_name='annotation_set')
    amount = models.PositiveIntegerField(default=1000, verbose_name='Сумма оплаты')
    method = models.CharField(choices=FREQUENCY_CHOICES,
                              default='1',
                              verbose_name='Способ оплаты: наличные или перевод на счет')
    price_id = models.CharField(max_length=100, **NULLABLE, verbose_name='ID цены')
    product_id = models.CharField(max_length=100, **NULLABLE, verbose_name='ID банковского продукта')
    payment_status = models.CharField(max_length=100, **NULLABLE, default='unpaid', verbose_name='Статус платежа')
    session_id = models.TextField(**NULLABLE, verbose_name='ID сессии')

    def __str__(self):
        return f'User: {self.user} paid behind {self.course} or {self.lesson} '

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежы'
