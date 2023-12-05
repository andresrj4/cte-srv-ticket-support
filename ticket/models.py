from django.db import models
from django.contrib.auth import get_user_model
from inventory.models import InventoryItem

User = get_user_model()

class Ticket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    engineer = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='engineer', null=True, blank=True)
    ticket_id = models.CharField(max_length=15, unique=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.TextField()
    status = models.CharField(max_length=20, choices=(('Active','Active'),('Pending','Pending'),('Resolved','Resolved')), default='Pending')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_resolved = models.BooleanField(default=False)
    severity = models.CharField(max_length=5, choices=(('1','1'),('2','2'),('3','3')), null=True, blank=True)
    is_assigned_to_engineer = models.BooleanField(default=False)
    resolution_steps = models.TextField(blank=True, null=True)
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, null=True, blank=True)
    survey_completed = models.BooleanField(default=False)

class InventoryItemTicket(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)

class SurveyResponse(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    satisfaction_score = models.IntegerField()
    comments = models.TextField()