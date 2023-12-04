from django.urls import path
from .views import view_inventory, add_inventory_item

urlpatterns = [
    path('view-inventory/', view_inventory, name='view-inventory'),
    path('add-inventory-item/', add_inventory_item, name='add-inventory-item'),
]