from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название магазина')
    address = models.CharField(max_length=255, verbose_name='Адрес магазина')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название продукта')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена продукта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
