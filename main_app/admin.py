from django.contrib import admin
from .models import Item, Invoice


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'price')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_price')


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Item, ItemAdmin)
