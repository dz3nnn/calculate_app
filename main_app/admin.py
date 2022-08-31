from django.contrib import admin
from .models import Item, Invoice, Sell
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


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Sell, SellAdmin)
