from django.http import JsonResponse
from .models import Item, Sell, Payment, Service
from django.shortcuts import render
from .classes import MonthItem

import datetime


def setup_rests(request):
    """ Update all items for set rest = count"""

    all_items = Item.objects.all()

    for item in all_items:
        item.rest = item.count
        item.save()

    return JsonResponse({'success': 'true'})


def index(request):
    return render(request, 'index.html', context={})


def month(request):
    items = []
    q = request.GET.get("q", None)

    if q:
        filter_date = _parse_date_from_q(q)
        sells = Sell.objects.filter(created_date__year__gte=filter_date.year,
                                    created_date__month__gte=filter_date.month,
                                    created_date__year__lte=filter_date.year,
                                    created_date__month__lte=filter_date.month)
        for sell in sells:
            item = _prepare_sell_to_month_item(sell)
            items.append(item)

        payments = Payment.objects.filter(created_date__year__gte=filter_date.year,
                                          created_date__month__gte=filter_date.month,
                                          created_date__year__lte=filter_date.year,
                                          created_date__month__lte=filter_date.month)

        for payment in payments:
            item = _prepare_payment_to_month_item(payment)
            items.append(item)

        services = Service.objects.filter(created_date__year__gte=filter_date.year,
                                          created_date__month__gte=filter_date.month,
                                          created_date__year__lte=filter_date.year,
                                          created_date__month__lte=filter_date.month)

        for service in services:
            item = _prepare_service_to_month_item(service)
            items.append(item)

    return render(request, 'month.html', context={'items': items, 'full_price': _calculate_full_price(items)})


def _parse_date_from_q(q):
    return datetime.datetime.strptime(q, "%Y-%m").date()


def _prepare_sell_to_month_item(sell):
    item = MonthItem(name=f'{sell.item.name} ({sell.count} шт.)',
                     price=_calc_sell_value(sell))
    return item


def _prepare_service_to_month_item(service_model):
    item = MonthItem(name=service_model.name, price=service_model.price)
    return item


def _prepare_payment_to_month_item(payment_model):
    item = MonthItem(name=payment_model.payment_type.name,
                     price=-abs(payment_model.price))
    return item


def _calc_sell_value(sell_model):
    return sell_model.count * (sell_model.price - sell_model.item.price)


def _calculate_full_price(items):
    full_price = 0
    for item in items:
        full_price += item.price
    return full_price
