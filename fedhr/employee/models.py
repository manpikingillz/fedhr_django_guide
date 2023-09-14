from decimal import Decimal
from django.db import models

from fedhr.common.models import BaseModel
from fedhr.setup.models import Country
from fedhr.files.models import File


class Employee(BaseModel):
    class Gender(models.TextChoices):
        FEMALE = 'FEMALE', 'Female'
        MALE = 'MALE', 'Male'

    class MaritalStatus(models.TextChoices):
        SINGLE = 'SINGLE', 'Single'
        MARRIED = 'MARRIED', 'Married'
        COMMON_LAW = 'COMMON_LAW', 'Common Law'
        DOMESTIC_PARTNERSHIP = 'DOMESTIC_PARTNERSHIP', 'Domestic Partnership'

    # Basic Information
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    preferred_name = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(choices=Gender.choices, null=True, blank=True, max_length=6)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    marital_status = models.CharField(choices=MaritalStatus.choices, null=True, blank=True, max_length=50)
    nationality = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    avatar = models.ForeignKey(
        File,
        related_name='employee_avatars',
        on_delete=models.SET_NULL,
        null=True, blank=True
    )
    # Job
    hire_date = models.DateTimeField(null=True, blank=True)

    # Identification Information
    social_security_number = models.CharField(max_length=50, null=True, blank=True)
    national_identification_number = models.CharField(max_length=50, null=True, blank=True)
    tax_identification_number = models.CharField(max_length=50, null=True, blank=True)

    # Contact Information
    email = models.CharField(max_length=255, null=True, blank=True)
    home_email = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=30, null=True, blank=True)
    work_phone = models.CharField(max_length=30, null=True, blank=True)
    home_phone = models.CharField(max_length=30, null=True, blank=True)

    # Address Information
    street1 = models.CharField(max_length=255, null=True, blank=True)
    street2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    # Social
    linked_in = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.middle_name or " "} {self.last_name}'

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.middle_name or " "} {self.last_name}'


class EducationAward(BaseModel):
    education_award_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.education_award_name


class Education(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=255)
    award = models.ForeignKey(EducationAward, on_delete=models.SET_NULL,null=True, blank=True)
    major = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    score = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return self.institution_name


class Visa(BaseModel):
    visa_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.visa_name


class VisaInformation(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    visa = models.ForeignKey(Visa, on_delete=models.SET_NULL, null=True, blank=True)
    issued_date = models.DateField(null=True, blank=True)
    issuing_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    expiration_date = models.DateField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.visa.visa_name if self.visa else ''


class EmploymentStatusType(BaseModel):
    employment_status_type_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.employment_status_type_name


class EmploymentStatus(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    effective_date = models.DateField(null=True, blank=True)
    employment_status_type = models.ForeignKey(EmploymentStatusType, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.employment_status_type.employment_status_type_name if self.employment_status_type else ''


class Location(BaseModel):
    location_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.location_name

class Division(BaseModel):
    division_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.division_name

class Department(BaseModel):
    department_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.department_name

class Job(BaseModel):
    job_title_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.job_title_name

class JobInformation(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    effective_date = models.DateField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department,  on_delete=models.SET_NULL, null=True, blank=True)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True, blank=True)
    reports_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, related_name="direct_reports", null=True, blank=True)

    def __str__(self) -> str:
        return self.job.job_title_name if self.job else ''

class Currency(BaseModel):
    currency_name = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=3)

    def __str__(self) -> str:
        return f'{self.currency_code} {self.currency_name}'

class ChangeReason(BaseModel):
    change_reason_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.change_reason_name

class Compensation(BaseModel):
    class PayType(models.TextChoices):
        SALARY = 'SALARY', 'Salary'
        HOURLY = 'HOURLY', 'Hourly'
        COMMISSION_ONLY = 'COMMISSION_ONLY', 'Commission Only'
    class PayRatePeriod(models.TextChoices):
        DAY = 'DAY', 'Day'
        WEEK = 'WEEK', 'Week'
        MONTH = 'MONTH', 'Month'
        QUARTER = 'QUARTER', 'Quarter'
        YEAR = 'Year'
        PAY_PERIOD = 'Pay Period'
        PIECE = 'Piece'
    class OvertimeStatus(models.TextChoices):
        EXEMPT = 'EXEMPT', 'Exempt'
        NON_EXEMPT = 'NON_EXEMPT', 'Non Exempt'

    class PaymentMethod(models.TextChoices):
        PAYCHECK = 'PAYCHECK', 'PAYCHECK'
        DIRECT_DEPOSIT = 'DIRECT_DEPOSIT', 'Direct Deposit'
        CASH = 'CASH', 'Cash'

    class PaySchedule(models.TextChoices):
        TWICE_A_MONTH = 'TWICE_A_MONTH', 'Twice a month'
        EVERY_OTHER_WEEK = 'EVERY_OTHER_WEEK', 'Every other week'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    effective_date = models.DateField(null=True, blank=True)
    pay_type = models.CharField(choices=PayType.choices, max_length=50)
    pay_rate = models.DecimalField(max_digits=12, decimal_places=2)
    pay_rate_currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True, blank=True)
    #only applicable for salary pay_type
    pay_rate_period = models.CharField(choices=PayRatePeriod.choices, max_length=50)

    pay_schedule = models.CharField(choices=PaySchedule.choices, null=True, blank=True, max_length=50) # e.g once a month, twice a month, every other week
    overtime_status = models.CharField(choices=OvertimeStatus.choices, null=True, blank=True, max_length=50)
    change_reason = models.ForeignKey(ChangeReason, on_delete=models.SET_NULL, null=True, blank=True)
    payment_method = models.CharField(choices=PaymentMethod.choices, max_length=50)
    comment = models.TextField(null=True, blank=True)

class EmergencyContact(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    relationship = models.CharField(max_length=255, null=True, blank=True)
    mobile_phone = models.CharField(max_length=50, null=True, blank=True)
    home_phone = models.CharField(max_length=50, null=True, blank=True)
    work_phone = models.CharField(max_length=50, null=True, blank=True)
    home_email = models.CharField(max_length=50, null=True, blank=True)
    work_email = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='emergency_contacts')
    is_primary_contact = models.BooleanField(default=False)

class Dependant(BaseModel):
    class Gender(models.TextChoices):
        FEMALE = 'FEMALE', 'Female'
        MALE = 'MALE', 'Male'
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    national_identification_number = models.CharField(max_length=50, null=True, blank=True)
    gender =  models.CharField(choices=Gender.choices, max_length=6)
    relationship = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=100, null=True, blank=True)
    nationality = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name="dependants")


class Note(BaseModel):
     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
     note = models.TextField()

# TODO: Implement Employee Documents. Check Zenefits