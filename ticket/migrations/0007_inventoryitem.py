# Generated by Django 4.1.13 on 2023-12-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_alter_ticket_severity'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, choices=[('Software', 'Software'), ('Hardware', 'Hardware')], max_length=50, null=True)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
