# Generated by Django 2.2.8 on 2020-03-04 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=256)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('High Priority', 'Высокий приоритет'), ('Medium Priority', 'Средний приоритет'), ('Low Priority', 'Низкий приоритет')], default='Medium Priority', max_length=128)),
                ('count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Приоритет',
                'verbose_name_plural': 'Приоритеты',
            },
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Выполнено')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='tasks.Category', verbose_name='Категория')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
                ('priority', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Priority', verbose_name='Приоритет')),
            ],
            options={
                'verbose_name': 'Задачу',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]