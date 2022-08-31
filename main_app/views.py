from django.http import JsonResponse
from .models import Item
from django.shortcuts import render


def setup_rests(request):
    """ Update all items for set rest = count"""

    all_items = Item.objects.all()

    for item in all_items:
        item.rest = item.count
        item.save()

    return JsonResponse({'success': 'true'})


def test(request):
    return render(request, 'month.html', {'test': 'test'})
