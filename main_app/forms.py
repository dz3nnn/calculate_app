from django import forms
from .models import Sell, Item


class SellAdminForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        item_cleaned = cleaned_data.get('item')
        count_cleaned = cleaned_data.get('count')

        if item_cleaned and item_cleaned.rest < count_cleaned:
            raise forms.ValidationError("Недостаточно остатков.")
