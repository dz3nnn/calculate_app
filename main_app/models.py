from django.db import models
from django.utils.timezone import now


class Item(models.Model):
    """ Модель для товаров """
    name = models.CharField(verbose_name='Наименование', max_length=100)
    count = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(
        verbose_name='Цена закупки', max_digits=4, decimal_places=2)
    created_date = models.DateField(verbose_name='Дата',default=now)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
