from django.contrib import admin

from django.contrib import admin
from todolist.models import Task, TaskList


class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_description', 'task_due_date')
    search_fields = ('task_name',)
    list_filter = ('task_due_date',)
    ordering = ('task_due_date',)


class ListAdmin(admin.ModelAdmin):
    list_display = ('list_title',)


admin.site.register(Task, TaskAdmin)
admin.site.register(TaskList, ListAdmin)
