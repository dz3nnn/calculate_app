from django.http import JsonResponse
from .models import Item


def setup_rests(request):
    """ Update all items for set rest = count"""

    all_items = Item.objects.all()

    for item in all_items:
        item.rest = item.count
        item.save()

    return JsonResponse({'success': 'true'})
