from django.urls import path
from . import views

urlpatterns = [
    path('register-customer/', views.register_customer, name='register-customer'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change_password/', views.PasswordChangeView.as_view(template_name = "change_password.html"), name = "change-password")
]