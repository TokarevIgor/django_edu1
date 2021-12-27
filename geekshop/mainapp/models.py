from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, unique=True)
    description = models.TextField(
        verbose_name='описание', blank=True, null=True)
    img = models.ImageField(upload_to='category_images', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50, unique=True)
    category = models.ForeignKey(ProductCategory, verbose_name=(
        "категория продукта"), on_delete=models.SET_NULL, null=True)
    short_description = models.CharField(
        verbose_name=' короткое описание', blank=True, null=True, max_length=25)
    description = models.TextField(
        verbose_name='описание', blank=True, null=True)
    price = models.DecimalField(
        verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    price_with_discount = models.DecimalField(
        verbose_name='цена со скидкой', max_digits=8, decimal_places=2, default=0)
    img = models.ImageField(upload_to='products_images', blank=True)
    is_new = models.BooleanField(
        verbose_name='это новый продукт', default=False)
    is_popular = models.BooleanField(
        verbose_name='популярные товары', default=False)

    def __str__(self):
        return self.name
