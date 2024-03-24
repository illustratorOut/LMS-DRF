from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    photo = models.ImageField(upload_to='course/', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.__class__.__name__}({self.name} - {self.description})'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='lesson/', verbose_name='Превью', **NULLABLE)
    link_video = models.CharField(max_length=200, verbose_name='Ссылка на видео', **NULLABLE)
    linl_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.__class__.__name__}({self.name} - {self.description})'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Subscriptions(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    status = models.BooleanField(default=False, verbose_name='Подписан пользователь')

    def __str__(self):
        return f'{self.__class__.__name__}({self.user} - {self.course})'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
