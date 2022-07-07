from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукт'

