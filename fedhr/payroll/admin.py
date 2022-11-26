from django.contrib import admin

from fedhr.payroll.models import (
    PayrollPeriod, EmployeePayroll)


@admin.register(PayrollPeriod)
class PayrollPeriodAdmin(admin.ModelAdmin):
    fields = ('start_date', 'end_date')
    list_display = ('start_date', 'end_date')


@admin.register(EmployeePayroll)
class EmployeePayrollAdmin(admin.ModelAdmin):
    fields = (
        'payroll_period',
        'employee',
        'total_hours',
        'overtime_hours',
        'leave_hours',
        'gross_pay',
        'overtime_pay',
        'leave_pay'
        )
    list_display = (
        'payroll_period',
        'employee',
        'total_hours',
        'overtime_hours',
        'leave_hours',
        'gross_pay',
        'overtime_pay',
        'leave_pay'
        )
