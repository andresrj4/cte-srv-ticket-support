from django.contrib import admin
from .models import SurveyResponse

class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'customer', 'satisfaction_score', 'comments')