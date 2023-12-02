from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import PasswordChangeView
from .form import RegisterCustomerForm, PasswordChangingForm
from django.urls import reverse_lazy

User = get_user_model()


def register_customer(request):
    if request.method == "POST":
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.username = var.email
            var.save()
            messages.success(request, "Account created.")
            return redirect("login")
        else:
            messages.warning(request, "Something went wrong. Please try again.")
            return redirect("register-customer")
    else:
        form = RegisterCustomerForm()
        context = {"form": form}
        return render(request, "accounts/register_customer.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.warning(request, "Something went wrong. Please try again.")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Active session ended. Log in to continue")
    return redirect("login")


class PasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        messages.success(self.request, 'Password changed successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Password change failed. Please correct the errors and try again.')
        return super().form_invalid(form)
