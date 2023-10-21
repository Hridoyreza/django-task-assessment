from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'is_complete')
    list_filter = ('priority', 'is_complete')
    search_fields = ('title', 'description')
    ordering = ('priority',)  # Sort tasks by priority by default