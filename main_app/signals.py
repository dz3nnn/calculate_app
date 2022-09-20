from .models import Sell, Item
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=Sell)
def remove_rest_on_save(sender, instance, created, **kwargs):
    # Add new Sell -> remove rest from Item
    if created and instance.item:
        item_model = Item.objects.get(pk=instance.item.pk)
        item_model.rest -= instance.count
        item_model.save()


@receiver(post_delete, sender=Sell)
def add_rest_on_remove(sender, instance, **kwargs):
    # Delete Sell -> add rest to Item
    if instance.item:
        item_model = Item.objects.get(pk=instance.item.pk)
        # TODO: Check rest and count (rest <= count)
        item_model.rest += instance.count
        item_model.save()
