import random
import string
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import get_user_model
from .form import CreateTicketForm, AssignTicketForm, TicketResolutionForm
from .models import Ticket
from inventory.models import InventoryItem

User = get_user_model()

def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.customer = request.user
            while not var.ticket_id:
                id = ''.join(random.choices(string.digits, k=6))
                try:
                    var.ticket_id = id
                    var.save()
                    # sends email to customer (console)
                    subject = f'{var.ticket_title} #{var.ticket_id}'
                    message = 'Thanks you for submiting a ticket, we will assign an engineer soon.'
                    email_from = 'microtech@email.com'
                    recipient_list = [request.user.email, ]
                    send_mail(subject, message, email_from, recipient_list)
                    messages.success(request, 'Your ticket has been submitted. An engineer will reach out soon.')
                    return redirect('customer-active-tickets')
                except IntegrityError:
                    continue
        else:
            messages.warning(request, 'Something went wrong. Please check ticket form and try again.')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form':form}
        return render(request, 'ticket/create_ticket.html', context)

# customer all active tickets
def customer_active_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_active_tickets.html', context) 

# customer all resolved tickets
def customer_resolved_tickets(request):
    tickets = Ticket.objects.filter(customer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/customer_resolved_tickets.html', context) 

# engineer all assigned active tickets
def engineer_active_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=False).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/engineer_active_tickets.html', context) 

# engineer all assigned resolved tickets
def engineer_resolved_tickets(request):
    tickets = Ticket.objects.filter(engineer=request.user, is_resolved=True).order_by('-created_on')
    context = {'tickets':tickets}
    return render(request, 'ticket/engineer_resolved_tickets.html', context) 

#assign ticket to engineer
def assign_ticket(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    if request.method == 'POST':
        form = AssignTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_assigned_to_engineer = True
            var.status = 'Active'
            var.save()
            messages.success(request, f'Ticket assigned to {var.engineer}')
            return redirect('ticket-queue')
        else:
            messages.warning(request, 'Something went wrong. Check and try again.')
            return redirect('assign-ticket')
    else:
        form = AssignTicketForm(instance=ticket)
        form.fields['engineer'].queryset = User.objects.filter(is_engineer=True)
        context = {'form':form, 'ticket':ticket}
        return render(request, 'ticket/assign_ticket.html', context)
    
#ticket details
def ticket_details(request, ticket_id):
    ticket = Ticket.objects.get(ticket_id=ticket_id)
    context = {'ticket':ticket}
    return render(request, 'ticket/ticket_details.html', context)

#ticket queue (admin)
def ticket_queue(request):
    tickets = Ticket.objects.filter(is_assigned_to_engineer=False)
    context = {'tickets':tickets}
    return render(request, 'ticket/ticket_queue.html', context)

def resolve_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    inventory_items = InventoryItem.objects.all()

    if request.method == 'POST':
        form = TicketResolutionForm(request.POST)
        if form.is_valid():
            rs = form.cleaned_data['rs']
            inventory_item_id = form.cleaned_data['inventory_item'].id  # Extract the ID directly
            quantity_used = form.cleaned_data['quantity_used']

            inventory_item = get_object_or_404(InventoryItem, id=inventory_item_id)

            if inventory_item.quantity < quantity_used:
                messages.warning(request, 'Not enough quantity in inventory for the selected item.')
                return redirect('ticket-details', ticket_id=ticket_id)

            # Update the inventory item quantity
            inventory_item.quantity -= quantity_used
            inventory_item.save()

            # Update the ticket resolution
            ticket.resolution_steps = rs
            ticket.is_resolved = True
            ticket.status = 'Resolved'
            ticket.save()

            messages.success(request, 'Ticket has been marked as resolved and closed.')
            return redirect('dashboard')
    else:
        form = TicketResolutionForm()

    context = {'ticket': ticket, 'inventory_items': inventory_items, 'form': form}
    return render(request, 'ticket/resolve_ticket.html', context)
