import datetime
from colorama import Fore

from django.core.management import BaseCommand

from materials.models import Course, Lesson
from users.models import User, Payment


class Command(BaseCommand):
    def create_user(self):
        ''' Создаем пользователя '''
        dict_user = {
            'user_admin': {
                'email': 'admin@sky.pro',
                'first_name': 'Admin',
                'last_name': 'Adminov',
                'is_superuser': True,
                'is_staff': True,
                'is_active': True,
                'password': '1234S5678'},

            'user_moder': {
                'email': 'manager@sky.pro',
                'first_name': 'Manager',
                'last_name': 'Managers',
                'is_active': True,
                'password': '1234S5678'},

            'user_uses': {
                'email': 'user@sky.pro',
                'first_name': 'User',
                'last_name': 'Users',
                'is_active': True,
                'password': '1234S5678'},
        }

        list_user_ = []

        for row in dict_user:
            email = dict_user[row]['email']
            password = dict_user[row]['password']

            if User.objects.filter(email=email):
                print(f'Пользователь {Fore.RED}{email}{Fore.RESET} уже существует!')
            else:
                user = User.objects.create(**dict_user[row])
                user.set_password(password)
                user.save()
                print(f'Пользователь {Fore.GREEN}{email}{Fore.RESET} создан! ')
                list_user_.append(user)
        return list_user_

    def create_course(self):
        ''' Создаем курс '''

        course = [
            {
                'name': 'Python',
                'photo': 'course/Python.png',
                'description': 'Курс Python: Изучайте основы программирования с легкостью!'
            },
            {
                'name': 'Java',
                'photo': 'course/Java.png',
                'description': 'Курс Java: От новичка до профессионала'
            },
            {
                'name': 'PHP',
                'photo': 'course/PHP.png',
                'description': 'Курс PHP: Основы программирования'
            }]
        courses = [Course.objects.create(**i) for i in course]
        print(f'{Fore.GREEN}Cозданы курсы: {Fore.RESET}', *courses, sep='\n')
        return courses

    def create_lessons(self, course_):
        ''' Создаем урок '''

        lessons = [
            {
                'name': 'Урок Python с нуля #1',
                'description': 'Программирование на Питон для начинающих',
                'photo': 'course/Python.png',
                'link_video': 'https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa',
                'linl_course': course_[0],
            },
            {
                'name': 'Урок Java с нуля',
                'description': 'Программирование на Джава для начинающих',
                'photo': 'course/Java.png',
                'link_video': 'https://www.youtube.com/watch?v=U2OliQwRb6c&list=PLDyJYA6aTY1lT614ixLYq48har7EnCXpk',
                'linl_course': course_[1],
            },
            {
                'name': 'Урок PHP для начинающих',
                'description': 'Введение в язык PHP',
                'photo': 'course/PHP.png',
                'link_video': 'https://www.youtube.com/watch?v=GfHSbgyHN_I&list=PLDyJYA6aTY1m5zGQVcEYIoSFz2GD8u7cC',
                'linl_course': course_[2],
            },
            {
                'name': 'Уроки Python с нуля #2',
                'description': 'Установка среды разработки',
                'photo': 'course/Python.png',
                'link_video': 'https://www.youtube.com/watch?v=CfqX2_xY8VQ',
                'linl_course': course_[0],
            },
        ]
        lessons = [Lesson.objects.create(**i) for i in lessons]
        print(f'{Fore.GREEN}Созданы уроки: {Fore.RESET}', *lessons, sep='\n')
        return lessons

    def create_payments(self, user_, course_, lesson_):
        '''Создаем платеж'''

        payments = [
            {
                'user': user_[2],
                'date_payment': datetime.datetime.now().date(),
                'payment_course': course_[0],
                'payment_amount': 1000,
            },
            {
                'user': user_[2],
                'date_payment': datetime.datetime.now().date(),
                'payment_lesson': lesson_[1],
                'payment_amount': 800,
                'payment_method': '2',
            },
            {
                'user': user_[1],
                'date_payment': datetime.datetime.now().date(),
                'payment_lesson': lesson_[1],
                'payment_amount': 100,
            },
            {
                'user': user_[1],
                'date_payment': datetime.datetime.now().date(),
                'payment_course': course_[2],
                'payment_amount': 20000,
                'payment_method': '2',
            },
        ]

        payment = [Payment.objects.create(**i) for i in payments]

        print(f'{Fore.GREEN}Cозданы платежи: {Fore.RESET}', f'User:', *payment, sep='\n')

    def handle(self, *args, **options):

        list_user = self.create_user()
        list_course = self.create_course()
        list_lesson = self.create_lessons(list_course)

        users = User.objects.all()
        self.create_payments(users, list_course, list_lesson)
