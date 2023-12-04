from django import forms
from .models import InventoryItem

class AddInventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'quantity', 'category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = forms.Select(choices=InventoryItem.CATEGORY_CHOICES)