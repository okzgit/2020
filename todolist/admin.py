from django.contrib import admin
from .models import TaskList


# Register your models here.
class TaskListAdmin(admin.ModelAdmin):
    list_display = 'task', 'done', 'manager'


admin.site.register(TaskList, TaskListAdmin)

