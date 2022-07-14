from django.contrib import admin
from .models import Item, Invoice

admin.site.register([Item, Invoice])
