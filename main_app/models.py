from django.db import models
from django.utils.timezone import now
from django.contrib import admin


class Invoice(models.Model):
    """ Модель для накладных """
    name = models.CharField(verbose_name='Название документа', max_length=100)
    created_date = models.DateField(verbose_name='Дата', default=now)

    @property
    @admin.display(
        description='Стоимость накладной',
    )
    def full_price(self):
        items = Item.objects.filter(invoice=self)
        return sum([item.price for item in items])

    def __str__(self):
        return '%s (от %s)' % (self.name, self.created_date)

    class Meta:
        verbose_name = 'Накладная'
        verbose_name_plural = 'Накладные'


class Item(models.Model):
    """ Модель для товаров """
    name = models.CharField(verbose_name='Наименование', max_length=100)
    count = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(
        verbose_name='Цена закупки', max_digits=10, decimal_places=2)
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, verbose_name='Накладная', blank=True, null=True)
    created_date = models.DateField(verbose_name='Дата', default=now)

    def __str__(self):
        return '%s (количество: %s) - %s' % (self.name, self.count, self.created_date)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
