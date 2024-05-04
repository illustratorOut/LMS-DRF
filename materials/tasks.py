import colorama

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from materials.models import Course
from users.models import User


@shared_task
def send_mail_update_course(user_id, update_course_pk):
    '''Отправка сообщения по эл. почте'''
    print(f'{colorama.Fore.GREEN}Задача запущена{colorama.Fore.RESET}')
    subscribers = User.objects.filter(pk=user_id)[0]
    course = Course.objects.filter(pk=update_course_pk)[0]

    try:
        send_mail(
            subject='Обновление курса',
            message=f'Курс "{course.description}" на который вы подписаны обновлён',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[subscribers.email],
            fail_silently=True,
        )
    except Exception as e:
        print(f'Ошибка при отправке письма на email: {e}')


@shared_task
def checking_activity():
    users = User.objects.filter(is_active=True)
    for user in users:
        if user.last_login is not None and timezone.now() > user.last_login + timezone.timedelta(days=30):
            user.is_active = False
            user.save()
