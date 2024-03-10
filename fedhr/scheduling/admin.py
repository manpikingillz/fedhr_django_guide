from django.contrib import admin

from fedhr.scheduling.models import EmployeeShift, Shift, ShiftDaysAndTime


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    fields = ('shift_name', )
    list_display = ('shift_name', )


@admin.register(ShiftDaysAndTime)
class ShiftDaysAndTimeAdmin(admin.ModelAdmin):
    fields = ('shift', 'start_time', 'end_time', 'days')
    list_display = ('shift', 'start_time', 'end_time', 'days')


@admin.register(EmployeeShift)
class EmployeeShiftAdmin(admin.ModelAdmin):
    fields = ('employee', 'shift', 'effective_date', 'expiry_date')
    list_display = ('employee', 'shift', 'effective_date', 'expiry_date')

