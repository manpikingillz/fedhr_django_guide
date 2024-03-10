from django.contrib import admin

from fedhr.timesheet.models import TimeRecord
from fedhr.timesheet.models import Task


@admin.register(TimeRecord)
class TimeRecordAdmin(admin.ModelAdmin):
    fields = (
        'employee',
        'work_day',
        'clock_in',
        'clock_out',
        'duration',
        'work_or_break',
        'task'
    )
    list_display = (
        'employee',
        'work_day',
        'clock_in',
        'clock_out',
        'duration',
        'work_or_break',
        'task'
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'description',
        'assignee',
        'date_assigned',
        'date_due',
        'date_completed',
        'status'
    )
    list_display = (
        'title',
        'description',
        'assignee',
        'date_assigned',
        'date_due',
        'date_completed',
        'status'
    )