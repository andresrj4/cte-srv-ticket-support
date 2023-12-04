from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InventoryItem
from .form import AddInventoryItemForm

def view_inventory(request):
    inventory_items = InventoryItem.objects.all()
    return render(request, 'inventory/view_inventory.html', {'inventory_items': inventory_items})

def add_inventory_item(request):
    if request.method == 'POST':
        form = AddInventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inventory item added successfully.')
            return redirect('view-inventory')
        else:
            messages.warning(request, 'Error adding inventory item. Check the form and try again.')
    else:
        form = AddInventoryItemForm()

    return render(request, 'inventory/add_inventory_item.html', {'form': form})