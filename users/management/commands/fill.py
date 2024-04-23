import datetime
from colorama import Fore
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

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
                print(
                    f'Пользователь {Fore.GREEN}{email}{Fore.RESET} создан! password: {Fore.GREEN}1234S5678{Fore.RESET}')
                list_user_.append(user)
        return list_user_

    def create_course(self):
        ''' Создаем курс '''

        course = [
            {
                'name': 'Python',
                'photo': 'course/Python.png',
                'description': 'Курс Python: Изучайте основы программирования с легкостью!',
                'owner': User.objects.filter(email='user@sky.pro')[0],
            },
            {
                'name': 'Java',
                'photo': 'course/Java.png',
                'description': 'Курс Java: От новичка до профессионала',
                'owner': User.objects.filter(email='manager@sky.pro')[0],
            },
            {
                'name': 'PHP',
                'photo': 'course/PHP.png',
                'description': 'Курс PHP: Основы программирования',
                'owner': User.objects.filter(email='manager@sky.pro')[0],
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
                'owner': User.objects.filter(email='manager@sky.pro')[0],
            },
            {
                'name': 'Урок Java с нуля',
                'description': 'Программирование на Джава для начинающих',
                'photo': 'course/Java.png',
                'link_video': 'https://www.youtube.com/watch?v=U2OliQwRb6c&list=PLDyJYA6aTY1lT614ixLYq48har7EnCXpk',
                'linl_course': course_[1],
                'owner': User.objects.filter(email='manager@sky.pro')[0],
            },
            {
                'name': 'Урок PHP для начинающих',
                'description': 'Введение в язык PHP',
                'photo': 'course/PHP.png',
                'link_video': 'https://www.youtube.com/watch?v=GfHSbgyHN_I&list=PLDyJYA6aTY1m5zGQVcEYIoSFz2GD8u7cC',
                'linl_course': course_[2],
                'owner': User.objects.filter(email='manager@sky.pro')[0],
            },
            {
                'name': 'Уроки Python с нуля #2',
                'description': 'Установка среды разработки',
                'photo': 'course/Python.png',
                'link_video': 'https://www.youtube.com/watch?v=CfqX2_xY8VQ',
                'linl_course': course_[0],
                'owner': User.objects.filter(email='user@sky.pro')[0],
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
                'course': course_[0],
                'amount': 1000,
            },
            {
                'user': user_[2],
                'date_payment': datetime.datetime.now().date(),
                'lesson': lesson_[1],
                'amount': 800,
                'method': '2',
            },
            {
                'user': user_[1],
                'date_payment': datetime.datetime.now().date(),
                'lesson': lesson_[1],
                'amount': 100,
            },
            {
                'user': user_[1],
                'date_payment': datetime.datetime.now().date(),
                'course': course_[2],
                'amount': 20000,
                'method': '2',
            },
        ]

        payment = [Payment.objects.create(**i) for i in payments]

        print(f'{Fore.GREEN}Cозданы платежи: {Fore.RESET}', f'User:', *payment, sep='\n')

    def add_group(self, name_group):
        ''' Создаем Groups() Пример:Менеджер '''
        try:
            manager_group = Group.objects.get_or_create(name=name_group)
            print(f'\nГруппа' + Fore.GREEN + f' "{name_group}" ' + Fore.RESET + 'созданна!')
        except:
            print(f'Группа {Fore.RED}{name_group}{Fore.RESET} уже существует!')
        return manager_group

    def add_permissions(self, name_group: str):
        manager_group = Group.objects.filter(name=name_group).get()
        print(f'Группе {Fore.GREEN} "{name_group}" {Fore.RESET} добавленны права:')

        ct = ContentType.objects.get_for_model(Course)
        post_permission = Permission.objects.filter(content_type=ct)
        for perm in post_permission:
            if perm.codename in ["view_course", "change_course"]:
                manager_group.permissions.add(perm)
                print(f'+ {Fore.GREEN}{perm}{Fore.RESET}')

        ct = ContentType.objects.get_for_model(Lesson)
        post_permission = Permission.objects.filter(content_type=ct)
        for perm in post_permission:
            if perm.codename in ["view_lesson", "change_lesson"]:
                manager_group.permissions.add(perm)
                print(f'+ {Fore.GREEN}{perm}{Fore.RESET}')

    def handle(self, *args, **options):

        list_user = self.create_user()
        list_course = self.create_course()
        list_lesson = self.create_lessons(list_course)

        users = User.objects.all()
        self.create_payments(users, list_course, list_lesson)

        # Менеджер -> group(Модератор)
        self.add_group('Модератор')
        self.add_permissions('Модератор')
        user = User.objects.get(email='manager@sky.pro')
        my_group = Group.objects.get(name='Модератор')
        my_group.user_set.add(user)
        print(
            f'\nПользователю: ' + Fore.MAGENTA + f'{user}' + Fore.RESET + f' присвоены права - ' + Fore.GREEN + f'"{my_group}"' + Fore.RESET)
