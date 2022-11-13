from django.contrib import admin

from fedhr.timeoff.models import AccrualMilestone, Holiday, LeaveBalance, LeaveCategory, LeavePolicy, LeaveRequest, WorkWeek


@admin.register(LeaveCategory)
class LeaveCategoryAdmin(admin.ModelAdmin):
    fields = (
        'leave_category_name',
        'is_paid',
        'is_visible_calendar',
        'track_time_in',
        'color',
        'icon',
        'removed'
    )

    list_display = (
        'leave_category_name',
        'is_paid',
        'is_visible_calendar',
        'track_time_in',
        'color',
        'icon',
        'removed'
    )


@admin.register(LeavePolicy)
class LeavePolicyAdmin(admin.ModelAdmin):
    fields = (
        'leave_policy_name',
        'leave_category',
        'carry_over_month',
        'carry_over_month_day',
        'is_negative_balance_limit_on',
        'negative_balance_limit',
        'reset_negative_balances_to_zero_on_carry_over_day',
        'is_first_accrual_prorated',
        'accrual_time_received_at_start_or_end',
        'is_transition_to_next_milestone_immediate',
        'employees'
    )
    list_display = (
        'leave_policy_name',
        'leave_category')


@admin.register(AccrualMilestone)
class AccrualMilestoneAdmin(admin.ModelAdmin):
    fields = (
        'accrual_milestone_name',
        'leave_policy',
        'accrued_amount',
        'policy_start_date',
        'accrual_frequency',
        'weekly_day',
        'every_other_week_day',
        'every_other_week_day_start',
        'twice_amonth_day1',
        'twice_amonth_day2',
        'monthly_day',
        'quartely_quarter1_month',
        'quartely_quarter1_month_day',
        'quartely_quarter2_month',
        'quartely_quarter2_month_day',
        'quartely_quarter3_month',
        'quartely_quarter3_month_day',
        'quartely_quarter4_month',
        'quartely_quarter4_month_day',
        'twice_ayear_first_half_month',
        'twice_ayear_first_half_month_day',
        'twice_ayear_second_half_month',
        'twice_ayear_second_half_month_day',
        'yearly_month',
        'yearly_month_day',
        'is_waiting_period_on',
        'waiting_period',
        'waiting_period_unit',
        'is_accrual_balance_limit_on',
        'accrual_balance_limit',
        'carry_over_unused_time_off_after_carry_over_date',
        'is_carry_over_unused_time_off_limit_on',
        'carry_over_unused_time_off_up_to'
    )
    list_display = (
        'accrual_milestone_name',
        'leave_policy',
        'accrued_amount',
        'policy_start_date',
    )


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    fields = (
        'employee',
        'leave_category',
        'from_date',
        'to_date',
        'amount',
        'reason',
        'status',
        'removed'
    )
    list_display = (
        'employee',
        'leave_category',
        'from_date',
        'to_date',
        'amount',
        'reason',
        'status'
    )


@admin.register(LeaveBalance)
class LeaveBalanceAdmin(admin.ModelAdmin):
    fields = (
        'employee',
        'leave_category',
        'current_balance',
        'used',
        'removed'
    )
    list_display = (
        'employee',
        'leave_category',
        'current_balance',
        'used'
    )


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    fields = (
        'holiday_name',
        'observed_date',
        'employees',
        'removed'
    )
    list_display = (
        'holiday_name',
        'observed_date'
    )


@admin.register(WorkWeek)
class WorkWeekAdmin(admin.ModelAdmin):
    fields = (
        'work_week',
        'hours_per_workday',
        'removed'
    )
    list_display = (
        'work_week',
        'hours_per_workday',
        'removed'
    )
