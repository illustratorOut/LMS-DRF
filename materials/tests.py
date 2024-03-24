from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


class TestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user@test.ru')
        self.moderator = User.objects.create(email='moderator@test.ru')
        self.course = Course.objects.create(
            name='Python',
            photo='course/Python.png',
            description='Курс Python: Изучайте основы программирования с легкостью!',
            owner=self.user,
        )
        self.lesson = Lesson.objects.create(
            name='Test name',
            description='Test description',
            photo='course/Python.png',
            link_video='https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa',
            linl_course=self.course,
            owner=self.user,
        )
        self.lesson2 = Lesson.objects.create(
            name='Урок Java с нуля',
            description='Программирование на Джава для начинающих',
            photo='course/Java.png',
            link_video='https://www.youtube.com/watch?v=U2OliQwRb6c&list=PLDyJYA6aTY1lT614ixLYq48har7EnCXpk',
            linl_course=self.course,
            owner=self.moderator,
        )

    def test_get_lesson(self):
        self.client.force_authenticate(user=self.user)

        resource = self.client.get(
            '/materials/'
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_200_OK
        )

    def test_get_detail_lesson(self):
        self.client.force_authenticate(user=self.user)

        resource = self.client.get(
            f'/materials/{self.lesson.pk}/'
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_200_OK
        )

    def test_post_lesson(self):
        self.client.force_authenticate(user=self.user)
        image_path = './media/course/Python.png'
        date = {
            'name': 'Test name',
            'description': 'Test description',
            'photo': SimpleUploadedFile(
                name='test_image.jpg',
                content=open(image_path, 'rb').read(),
                content_type='image/jpeg'
            ),
            'link_video': 'https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa',
            'linl_course': self.course.pk,
            'owner': self.user.pk,
        }

        resource = self.client.post(
            '/materials/create/',
            data=date,
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_201_CREATED,
        )

    def test_patch_lesson(self):
        self.client.force_authenticate(user=self.user)

        resource = self.client.patch(
            f'/materials/update/{self.lesson.pk}/',
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_200_OK,
        )

        resource = self.client.patch(
            f'/materials/update/{self.lesson2.pk}/',
        )
        self.assertEquals(
            resource.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.user)

        resource = self.client.delete(
            f'/materials/delete/{self.lesson.pk}/',
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        resource = self.client.patch(
            f'/materials/delete/{self.lesson2.pk}/',
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    def test_get_subscriptions(self):
        self.client.force_authenticate(user=self.user)

        resource = self.client.get(
            '/materials/subscriptions/'
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_200_OK
        )

    def test_post_subscriptions(self):
        self.client.force_authenticate(user=self.user)

        date = {
            'user': self.user.pk,
            'course': self.course.pk,
        }

        resource = self.client.post(
            '/materials/subscriptions/create/',
            data=date,
        )

        self.assertEquals(
            resource.status_code,
            status.HTTP_200_OK,
        )