from django.db import models

class InventoryItem(models.Model):
    CATEGORY_CHOICES = [
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
    ]

    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)