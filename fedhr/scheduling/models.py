from django.db import models
from django.contrib.postgres.fields import ArrayField

from fedhr.common.models import BaseModel
from fedhr.employee.models import Employee


class Shift(BaseModel):
    shift_name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f'{self.shift_name}'


class ShiftDaysAndTime(BaseModel):
    shift = models.ForeignKey(
        Shift, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days = ArrayField(
        models.PositiveSmallIntegerField(),
        size=7, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.shift} : {self.start_time} - {self.end_time}'


class EmployeeShift(BaseModel):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        related_name="employee_shifts")
    shift = models.ForeignKey(
        Shift, on_delete=models.CASCADE,
        related_name="employee_shifts")
    effective_date = models.DateTimeField()
    expiry_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{str(self.employee)} -> {str(self.shift)}'
