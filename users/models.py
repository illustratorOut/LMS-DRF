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
    payment_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Оплаченный курс', **NULLABLE)
    payment_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Оплаченный урок', **NULLABLE)
    payment_amount = models.IntegerField(verbose_name='Сумма оплаты')
    payment_method = models.CharField(choices=FREQUENCY_CHOICES,
                                      default='1',
                                      verbose_name='Способ оплаты: наличные или перевод на счет')

    def __str__(self):
        return f'User: {self.user} paid behind {self.payment_course} or {self.payment_lesson} '

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежы'
