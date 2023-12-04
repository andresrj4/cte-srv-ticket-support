# Generated by Django 4.1.13 on 2023-12-04 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_initial'),
        ('ticket', '0008_remove_inventoryitem_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InventoryItem',
            new_name='InventoryItemTicket',
        ),
        migrations.AddField(
            model_name='ticket',
            name='inventory_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.inventoryitem'),
        ),
    ]