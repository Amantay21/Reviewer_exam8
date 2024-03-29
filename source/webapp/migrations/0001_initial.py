# Generated by Django 4.2.1 on 2024-01-13 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('category', models.CharField(max_length=200, verbose_name='Категория товара')),
                ('description', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Описание')),
                ('image', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Автор')),
                ('description', models.TextField(blank=True, max_length=10000, null=True, verbose_name='Описание')),
                ('grade', models.IntegerField(verbose_name='Оценка')),
                ('moderation', models.BooleanField(default=False, verbose_name='Модерация')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.product', verbose_name='Продукт')),
            ],
        ),
    ]
