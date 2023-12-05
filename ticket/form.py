from django import forms
from .models import Ticket, InventoryItem


class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_title', 'ticket_description']

class AssignTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['engineer','severity']

class TicketResolutionForm(forms.Form):
    rs = forms.CharField(widget=forms.Textarea, label="Resolution Steps", required=False)
    inventory_item = forms.ModelChoiceField(queryset=InventoryItem.objects.all(), label="Select Inventory Item")
    quantity_used = forms.IntegerField(label="Quantity Used", required=False)

class SurveyForm(forms.Form):
    satisfaction_score = forms.IntegerField(label='Satisfaction Score', min_value=1, max_value=5)
    comments = forms.CharField(widget=forms.Textarea, label='Comments')
