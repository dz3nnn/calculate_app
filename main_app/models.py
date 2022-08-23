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
        return sum([item.price * item.count for item in items])

    def __str__(self):
        return '%s (от %s)' % (self.name, self.created_date)

    class Meta:
        verbose_name = 'Накладная'
        verbose_name_plural = 'Накладные'


class Item(models.Model):
    """ Модель для товаров """
    name = models.CharField(verbose_name='Наименование', max_length=100)
    count = models.IntegerField(verbose_name='Количество')
    rest = models.IntegerField(verbose_name='Остаток', default=0)
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

    def save(self, *args, **kwargs):
        if not self.rest:
            self.rest = self.count
        super(Item, self).save(*args, **kwargs)


class Sell(models.Model):
    """ Модель продажи товара """

    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, verbose_name='Товар', blank=True, null=True)
    count = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(
        verbose_name='Цена продажи', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def save(self, *args, **kwargs):
        if self.item:
            item_model = Item.objects.get(pk=self.item.pk)
            if item_model.rest >= self.count:
                item_model.rest -= self.count
                item_model.save()
                super(Sell, self).save(*args, **kwargs)
        else:
            # Can't sell
            pass
