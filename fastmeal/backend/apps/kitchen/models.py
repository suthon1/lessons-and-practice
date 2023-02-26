from django.db import models

# model for product
class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=30)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фото', upload_to='products/images/')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['category', 'is_available']

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=40, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    order_number = models.PositiveSmallIntegerField(blank=True, null=True)
    icon = models.ImageField(upload_to='category/img/')


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-order_number']


    def __str__(self) -> str:
        return f"{self.name} - {self.id}"