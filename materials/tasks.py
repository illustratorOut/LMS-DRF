from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from dotenv import load_dotenv

import os

load_dotenv()


@shared_task
def send_mail_update_course(subscribers, update_course):
    '''Отправка сообщения по эл. почте'''
    print(subscribers)
    for subscriber in subscribers:
        print('sdfdsf')
        print(subscriber)
        if subscriber.course.date_update < timezone.nou() + timezone.timedelta(hours=4):
            try:
                send_mail(
                    subject=f'Обновление курса "{update_course.name}"',
                    message=f'Курс "{update_course.name}" на который вы подписаны обновлён',
                    recipient_list=[subscriber.user.email],
                    from_email=os.getenv('YANDEX_MAIL'),
                    fail_silently=False,
                )
            except Exception as e:
                print(f'Ошибка при отправке письма на email: {e}')
