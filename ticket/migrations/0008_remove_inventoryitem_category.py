# Generated by Django 4.1.13 on 2023-12-04 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_inventoryitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='category',
        ),
    ]
