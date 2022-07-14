from django.contrib import admin
from .models import Item, Invoice


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'price')


admin.site.register([Invoice])
admin.site.register(Item, ItemAdmin)
