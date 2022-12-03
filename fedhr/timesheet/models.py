from django.db import models
from fedhr.common.models import BaseModel
from fedhr.employee.models import Employee


class Task(BaseModel):
    class TaskStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        DOING = 'DOING', 'Doing'
        DONE = 'DONE', 'Done'

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    assignee = models.ForeignKey(
        Employee, on_delete=models.SET_NULL,
        related_name='tasks', null=True, blank=True)
    date_assigned = models.DateTimeField(null=True, blank=True)
    date_due = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        choices=TaskStatus.choices,
        null=True, blank=True, max_length=20)

    def __str__(self) -> str:
        return self.title


class TimeRecord(BaseModel):
    class WorkOrBreak(models.TextChoices):
        WORK = 'WORK', 'Work'
        BREAK = 'BREAK', 'Break'

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        related_name='time_records')
    work_day = models.DateField()
    clock_in = models.DateTimeField()
    clock_out = models.DateTimeField()
    duration = models.FloatField(default=0.0)
    work_or_break = models.CharField(
        choices=WorkOrBreak.choices,
        null=True, blank=True, max_length=20)
    task = models.ForeignKey(
        Task, on_delete=models.SET_NULL,
        related_name='time_records',
        null=True, blank=True)
