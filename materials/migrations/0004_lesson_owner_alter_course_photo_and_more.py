# Generated by Django 4.2.11 on 2024-03-16 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials', '0003_alter_course_photo_alter_lesson_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='course/', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='link_video',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='linl_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials.course', verbose_name='Курс'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='lesson/', verbose_name='Превью'),
        ),
    ]
