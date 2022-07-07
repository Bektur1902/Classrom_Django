from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model
from task import settings
from product.models import Product

User = get_user_model()
# Create your models here.


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    text = models.TextField(verbose_name='Текст')
    rating = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Обзор'
        verbose_name_plural = 'Обзор'


