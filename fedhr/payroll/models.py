from decimal import Decimal
from django.db import models
from fedhr.common.models import BaseModel
from fedhr.employee.models import Employee


class PayrollPeriod(BaseModel):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


# Create your models here.
class EmployeePayroll(BaseModel):
    payroll_period = models.ForeignKey(
        PayrollPeriod, on_delete=models.CASCADE,
        related_name='employee_payrolls')
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        related_name='employee_payrolls')
    total_hours = models.DecimalField(
        max_digits=10, decimal_places=5, default=Decimal(0))
    overtime_hours = models.DecimalField(
        max_digits=10, decimal_places=5, default=Decimal(0))
    leave_hours = models.DecimalField(
        max_digits=10, decimal_places=5, default=Decimal(0))
    gross_pay = models.DecimalField(
        max_digits=20, decimal_places=10, default=Decimal(0))
    overtime_pay = models.DecimalField(
        max_digits=20, decimal_places=10, default=Decimal(0))
    leave_pay = models.DecimalField(
        max_digits=20, decimal_places=10, default=Decimal(0))

# TODO: Add models to cater for;
# Earnings, Deductions, Garnishments, 
# ReImburesments,  EmployerContributions,
# IndividualTaxes, EmployerTaxes