from django.db import models
from django.db.models.query import Q
from django.contrib.postgres.fields import ArrayField

from fedhr.common.models import BaseModel
from fedhr.employee.models import Employee


class LeaveCategory(BaseModel):
    class TrackTimeIn(models.TextChoices):
        DAYS = 'DAYS', 'Days'
        HOURS = 'HOURS', 'Hours'
    leave_category_name = models.CharField(max_length=255)
    is_paid = models.BooleanField(default=False)
    is_visible_calendar = models.BooleanField(default=False)
    track_time_in = models.CharField(choices=TrackTimeIn.choices, max_length=10)
    color = models.CharField(max_length=10)
    icon = models.FileField(upload_to='all_uploads', blank=True, null=True)

    def __str__(self) -> str:
        return self.leave_category_name


class LeavePolicy(BaseModel):
    class AccrualRecievedStartOrEnd(models.TextChoices):
        START = 'START', 'Start'
        END = 'END', 'End'

    class MonthOfYear(models.TextChoices):
        JANUARY = 'JANUARY', 'January',
        FEBUARY = 'FEBUARY', 'February'
        MARCH = 'MARCH', 'March'
        APRIL = 'APRIL', 'April'
        MAY = 'MAY', 'May'
        JUNE = 'JUNE', 'June'
        JULY = 'JULY', 'July'
        AUGUST = 'AUGUST', 'August'
        SEPTEMBER = 'SEPTEMBER', 'September'
        OCTOBER = 'OCTOBER', 'October'
        NOVEMBER = 'NOVEMBER', 'November'
        DECEMBER = 'DECEMBER', 'December'

    leave_policy_name = models.CharField(max_length=255)
    leave_category = models.ForeignKey(
        LeaveCategory, on_delete=models.CASCADE)

    # CARRYOVER DATE.
    carry_over_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True
    )
    carry_over_month_day = models.PositiveSmallIntegerField(null=True, blank=True)

    # NEGATIVE BALANCE
    # ###----------------------------------------------------------------
    # If the negative balance limit is not on, it means people can
    # have unlimited negative balances.
    is_negative_balance_limit_on = models.BooleanField(default=False)
    # What's the acceptable limit for negative balances? e.g Someone is taking leave,
    # but have 0 balance, they can request 5 days and that means they will have -5 as balance once it's approved.
    # So, is there a limit to what this negative value could be?
    negative_balance_limit = models.PositiveSmallIntegerField(
        null=True, blank=True)
    reset_negative_balances_to_zero_on_carry_over_day = models.BooleanField(
        default=False)

    # NEW HIRE PRORATION
    # Let's say the employee joined mid year, and the accrual period is a year,
    # should they receive all the time accrued for the year irrespective of their
    # joining date? or should we prorate based on the joining date and they will
    # receive only the accrued time starting from their joining date?
    is_first_accrual_prorated = models.BooleanField(
        default=False
    )

    # ACCRUAL TIMING
    # Should accrued time be received at the start or end of accrual period?
    accrual_time_received_at_start_or_end = models.CharField(
        choices=AccrualRecievedStartOrEnd.choices,
        max_length=20, null=True, blank=True
    )
    # should the accrual rules for the next milestone kick in
    # the day that the employee becomes eligible for the next milestone or
    # should the transition not begin until the end of the accrual period
    # that the employee became eligible for.
    is_transition_to_next_milestone_immediate = models.BooleanField(
        default=False
    )

    employees = models.ManyToManyField(
        Employee, related_name='leave_policies')

    def __str__(self) -> str:
        return self.leave_policy_name

    # TODO: Implement accrual validations


class AccrualMilestone(BaseModel):
    class AccrualFrequency(models.TextChoices):
        DAILY = 'DAILY', 'Daily'
        WEEKLY = 'WEEKLY', 'Weekly'
        EVERY_OTHER_WEEK = 'EVERY_OTHER_WEEK', 'Every other week'
        TWICE_A_MONTH = 'TWICE_A_MONTH', 'Twice a month'
        MONTHLY = 'MONTHLY', 'Monthly'
        QUARTERLY = 'QUARTERLY', 'Quartely'
        TWICE_A_AYEAR = 'TWICE_A_AYEAR', 'Twice a year'
        YEARLY = 'YEARLY', 'Yearly'
        ON_HIRE_DATE_ANNIVERSARY = 'ON_HIRE_DATE_ANNIVERSARY', 'On Hire Date Anniversary'
        PER_HOUR_WORKED = 'PER_HOUR_WORKED', 'Per hour worked'

    class DayOfWeek(models.TextChoices):
        MONDAY = 'MONDAY', 'Monday'
        TUESDAY = 'TUESDAY', 'Tuesday'
        WEDNESDAY = 'WEDNESDAY', 'Wednesday'
        THURSDAY = 'THURSDAY', 'Thursday'
        FRIDAY = 'FRIDAY', 'Friday'
        SATURDAY = 'SATURDAY', 'Saturday'
        SUNDAY = 'SUNDAY', 'Sunday'

    class MonthOfYear(models.TextChoices):
        JANUARY = 'JANUARY', 'January',
        FEBUARY = 'FEBUARY', 'February'
        MARCH = 'MARCH', 'March'
        APRIL = 'APRIL', 'April'
        MAY = 'MAY', 'May'
        JUNE = 'JUNE', 'June'
        JULY = 'JULY', 'July'
        AUGUST = 'AUGUST', 'August'
        SEPTEMBER = 'SEPTEMBER', 'September'
        OCTOBER = 'OCTOBER', 'October'
        NOVEMBER = 'NOVEMBER', 'November'
        DECEMBER = 'DECEMBER', 'December'

    class EveryOtherWeekDayStart(models.TextChoices):
        IMMEDIATE = 'IMMEDIATE', 'Immediate'
        NEXT = 'NEXT', 'Next'

    class WaitingPeriodUnit(models.TextChoices):
        DAYS = 'DAYS', 'Days'
        WEEKS = 'WEEKS', 'Weeks'
        MONTHS = 'MONTHS', 'Months'
        YEARS = 'YEARS', 'Years'

    accrual_milestone_name = models.CharField(
        max_length=255)
    leave_policy = models.ForeignKey(
        LeavePolicy, on_delete=models.CASCADE,
        null=True, blank=True)
    accrued_amount = models.FloatField()
    # Used in some cases where necessary.
    policy_start_date = models.DateTimeField(null=True, blank=True)

    # ACCRUAL FREQUENCY
    # ###----------------------------------------------------------------
    # TODO: Show accrual schedule previow in frontend.
    accrual_frequency = models.CharField(
        choices=AccrualFrequency.choices,
        max_length=50)
    weekly_day = models.CharField(
        choices=DayOfWeek.choices,
        max_length=50, null=True, blank=True)
    every_other_week_day = models.CharField(
        choices=DayOfWeek.choices,
        max_length=50, null=True, blank=True)
    # If we go with every_other_week_day, and say we chose mondays,
    # today is Fri 11 Nov 2022, but we may want to start
    # with the immediate monday of 14th or we may want to start
    # with the next monday of 21st
    # TODO: Evaluate if this field needs to stay or we could just use policy_start_date?
    every_other_week_day_start = models.CharField(
        choices=EveryOtherWeekDayStart.choices,
        max_length=50, null=True, blank=True)
    # Day should be in the first 15 days of the month
    twice_amonth_day1 = models.IntegerField(null=True, blank=True)
    # Day should be in the last 15 days of the month
    twice_amonth_day2 = models.IntegerField(null=True, blank=True)
    monthly_day = models.IntegerField(null=True, blank=True)
    # Month should be January to March
    quartely_quarter1_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True)
    quartely_quarter1_month_day = models.PositiveSmallIntegerField(
        null=True, blank=True)
    # Month should be Aprl to June
    quartely_quarter2_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True)
    quartely_quarter2_month_day = models.PositiveSmallIntegerField(
        null=True, blank=True)
    # Month should be July to September
    quartely_quarter3_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True)
    quartely_quarter3_month_day = models.PositiveSmallIntegerField(
        null=True, blank=True)
    # Month should be October to December
    quartely_quarter4_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True)
    quartely_quarter4_month_day = models.PositiveSmallIntegerField(
        null=True, blank=True)
    # Month should be January to June
    twice_ayear_first_half_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True)
    twice_ayear_first_half_month_day = models.PositiveSmallIntegerField(
        null=True, blank=True)
    # Month should be July to December
    twice_ayear_second_half_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True)
    twice_ayear_second_half_month_day = models.PositiveSmallIntegerField(
        null=True, blank=True)
    yearly_month = models.CharField(
        choices=MonthOfYear.choices,
        max_length=20, null=True, blank=True)
    yearly_month_day = models.PositiveSmallIntegerField(
        null=True, blank=True)

    # Accrual Options
    # WAITING PERIOD
    # ###----------------------------------------------------------------
    # Is there a waiting period before new employees begin accruing time?
    is_waiting_period_on = models.BooleanField(default=False)
    waiting_period = models.PositiveSmallIntegerField(
        null=True, blank=True)
    waiting_period_unit = models.CharField(
        choices=WaitingPeriodUnit.choices,
        max_length=10, null=True, blank=True)

    # MAXIMUM BALANCE
    # ###----------------------------------------------------------------
    # Is there a cap on the balance an employee can accrue? (Bamb analogy)
    # As in, employees can not have a balance greater than specified at any time. (Zenef analogy)
    is_accrual_balance_limit_on = models.BooleanField(default=False)
    accrual_balance_limit = models.FloatField(null=True, blank=True)

    # IS CARRYOVER ON OR OFF?
    # Can unused time off be carried over after the carryover date?
    carry_over_unused_time_off_after_carry_over_date = models.BooleanField(
        default=False)

    # CARRYOVER LIMIT / CAP
    # Employees can carry over up to (specificied number)
    # from one year to the next on the specified month and day.
    is_carry_over_unused_time_off_limit_on = models.BooleanField(
        default=False)
    carry_over_unused_time_off_up_to = models.PositiveSmallIntegerField(
        null=True, blank=True)

    def __str__(self) -> str:
        return f'{str(self.leave_policy)} : {self.accrual_milestone_name}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="twice_amonth_day1_should_be_15th_and_below",
                check=Q(twice_amonth_day1__lte=15)
            ),
            models.CheckConstraint(
                name="twice_amonth_day2_should_be_above_15th",
                check=Q(twice_amonth_day2__gt=15)
            )
        ]


class LeaveRequest(BaseModel):
    class LeaveStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        APPROVED = 'APPROVED', 'Approved'
        REJECTED = 'REJECTED', 'Rejected'
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    leave_category = models.ForeignKey(LeaveCategory, on_delete=models.SET_NULL, null=True)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    amount = models.FloatField()
    reason = models.TextField()
    status = models.CharField(
        choices=LeaveStatus.choices,
        max_length=50, default=LeaveStatus.PENDING)

    def __str__(self) -> str:
        return f'{str(self.employee)} : {self.from_date} - {self.to_date}'


class LeaveBalance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_category = models.ForeignKey(
        LeaveCategory, on_delete=models.CASCADE)
    current_balance = models.FloatField(default=0)
    used = models.FloatField(default=0)

    def __str__(self) -> str:
        return f'{str(self.employee)}: {str(self.leave_category)} : {self.current_balance}'

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['employee', 'leave_category'],
                name='unique_employee_leave_category'
            )
        ]


class Holiday(BaseModel):
    holiday_name = models.CharField(max_length=255)
    observed_date = models.DateField()
    employees = models.ManyToManyField(
        Employee, related_name='holidays')

    def __str__(self) -> str:
        return self.holiday_name


class WorkWeek(BaseModel):
    work_week = ArrayField(models.PositiveSmallIntegerField(), size=7)
    hours_per_workday = models.PositiveSmallIntegerField()
