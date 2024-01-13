from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    category = models.CharField(max_length=200, verbose_name="Категория товара")
    description = models.TextField(max_length=10000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Изображение')

    def __str__(self):
        return self.title


class Reviews(models.Model):
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Продукт')
    description = models.TextField(max_length=10000, null=True, blank=True, verbose_name='Описание')
    grade = models.IntegerField(verbose_name="Оценка")
    moderation = models.BooleanField(default=False, verbose_name="Модерация")
    created_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Время обновления', auto_now=True)


