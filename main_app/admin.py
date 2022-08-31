from django.contrib import admin
from .models import Item, Invoice, Sell, PaymentType, Payment
from .forms import SellAdminForm


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'rest', 'count', 'price')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_price')


class SellAdmin(admin.ModelAdmin):
    form = SellAdminForm

    list_display = ('get_item_name', 'price', 'count', 'full_price')

    def get_item_name(self, obj):
        return obj.item.name
    get_item_name.short_description = 'Товар'


class PaymentAdmin(admin.ModelAdmin):

    list_display = ('get_paymenttype_name', 'get_date_format', 'price')

    def get_date_format(self, obj):
        return obj.created_date.strftime('%m.%Y')
    get_date_format.short_description = 'Дата'

    def get_paymenttype_name(self, obj):
        return obj.payment_type.name
    get_paymenttype_name.short_description = 'Товар'


class PaymentTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Sell, SellAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
