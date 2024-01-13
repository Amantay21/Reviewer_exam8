from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название категорий", unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    category = models.ForeignKey('webapp.Category', on_delete=models.RESTRICT, verbose_name="Категория")
    description = models.TextField(max_length=10000, null=True, blank=True, verbose_name='Описание')
    image = models.CharField(max_length=10000, null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Продукт',
                                related_name='reviews')
    description = models.TextField(max_length=10000, null=True, blank=True, verbose_name='Описание')
    grade = models.IntegerField(verbose_name="Оценка")
    moderation = models.BooleanField(default=False, verbose_name="Модерация")
    created_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Время обновления', auto_now=True)

    def __str__(self):
        return f"{self.id, self.author}"
