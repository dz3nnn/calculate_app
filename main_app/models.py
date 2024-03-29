from django.db import models
from django.utils.timezone import now
from django.contrib import admin
from django.contrib import messages
from django.core.exceptions import ValidationError


class Invoice(models.Model):

    name = models.CharField(verbose_name='Название документа', max_length=100)
    created_date = models.DateField(verbose_name='Дата', default=now)

    @property
    @admin.display(
        description='Стоимость накладной',
    )
    def full_price(self):
        items = Item.objects.filter(invoice=self)
        return sum([item.price * item.count for item in items])

    def __str__(self):
        return '%s (от %s)' % (self.name, self.created_date)

    class Meta:
        verbose_name = 'Накладная'
        verbose_name_plural = 'Накладные'


class Item(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=100)
    count = models.IntegerField(verbose_name='Количество')
    rest = models.IntegerField(verbose_name='Остаток', default=0)
    price = models.DecimalField(
        verbose_name='Цена закупки', max_digits=10, decimal_places=2)
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, verbose_name='Накладная', blank=True, null=True)
    created_date = models.DateField(verbose_name='Дата', default=now)

    def __str__(self):
        if self.invoice:
            return f'{self.name} {self.price} BYN ({self.invoice.name}) остаток: {self.rest}'
        return f'{self.name} остаток: {self.rest}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name']

    def save(self, *args, **kwargs):
        # if not self.rest:
        #     self.rest = self.count
        super(Item, self).save(*args, **kwargs)


class Sell(models.Model):

    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, verbose_name='Товар', blank=True, null=True)
    count = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(
        verbose_name='Цена продажи', max_digits=10, decimal_places=2)
    created_date = models.DateField(verbose_name='Дата', default=now)

    @property
    @admin.display(
        description='Итого',
    )
    def full_price(self):
        return self.price * self.count

    def __str__(self):
        return f'{self.item.name} ({self.price} * {self.count} = {self.full_price})'

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'


class PaymentType(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=100)

    class Meta:
        verbose_name = 'Тип платежа'
        verbose_name_plural = 'Типы платежей'

    def __str__(self):
        return self.name


class Payment(models.Model):

    payment_type = models.ForeignKey(
        PaymentType, on_delete=models.CASCADE, verbose_name='Тип платежа')
    created_date = models.DateField(verbose_name='Дата', default=now)
    price = models.DecimalField(
        verbose_name='Сумма', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Service(models.Model):

    name = models.CharField(verbose_name='Наименование', max_length=100)
    created_date = models.DateField(verbose_name='Дата', default=now)
    price = models.DecimalField(
        verbose_name='Сумма', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
