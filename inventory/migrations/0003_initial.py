# Generated by Django 4.1.13 on 2023-12-04 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0002_delete_inventoryitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware')], max_length=10)),
            ],
        ),
    ]
