from django.contrib import admin

from fedhr.employee.models import ChangeReason, Compensation, Currency, Department, Dependant, Division, Education, EducationAward, EmergencyContact, Employee, EmploymentStatus, EmploymentStatusType, Job, JobInformation, Location, Note, Visa, VisaInformation
from fedhr.employee.models import Relationship


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Personal', {
                'fields': (
                    'first_name',
                    'last_name',
                    'middle_name',
                    'preferred_name',
                    'gender',
                    'date_of_birth',
                    'marital_status',
                    'nationality',
                    'avatar'
                )
            }
        ),
        (
            'Job', {
                'fields': (
                    'hire_date',
                )
            }
        ),
        (
            'Identification', {
                'fields': (
                    'social_security_number',
                    'national_identification_number',
                    'tax_identification_number'
                )
            }
        ),
        (
            'Contact', {
                'fields': (
                    'email',
                    'home_email',
                    'mobile_number',
                    'work_phone',
                    'home_phone'
                )
            }
        ),
        (
            'Address', {
                'fields': (
                    'street1',
                    'street2',
                    'city',
                    'province',
                    'country',
                    'zip_code'
                )
            }
        ),
        (
            'Social', {
                'fields': (
                    'linked_in',
                    'facebook',
                    'twitter',
                    'instagram'
                )
            }
        ),
        (
            'Other', {
                'fields': (
                    'created_at',
                    'removed'
                )
            }
        )
    )
    list_display = (
        'id',
        'first_name',
        'last_name',
        'gender',
        'hire_date',
        'email'
    )
    list_filter = ('first_name', 'last_name', 'removed')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    fields = ('employee', 'institution_name', 'award',
              'major', 'start_date', 'end_date', 'score')
    list_display = ('employee', 'institution_name', 'award',
              'major', 'start_date', 'end_date', 'score')
    search_fields = ('institution_name', )

@admin.register(EducationAward)
class EducationAwardAdmin(admin.ModelAdmin):
    fields = ('education_award_name', )
    list_display = ('education_award_name', )

@admin.register(Visa)
class VisaAdmin(admin.ModelAdmin):
    fields = ('visa_name',)
    list_display = ['visa_name',]
    list_filter = ['visa_name', 'removed']

@admin.register(VisaInformation)
class VisaInformationAdmin(admin.ModelAdmin):
    fields = ('employee', 'date', 'visa',
              'issued_date', 'issuing_country',
              'expiration_date', 'note',)

    list_display = ('employee', 'date', 'visa',
              'issued_date', 'issuing_country',
              'expiration_date', 'note' )
    list_filter = ['employee', 'removed']

@admin.register(EmploymentStatusType)
class EmploymentStatusTypeAdmin(admin.ModelAdmin):
    fields = ('employment_status_type_name', )
    list_display = ('employment_status_type_name', )

@admin.register(EmploymentStatus)
class EmploymentStatusAdmin(admin.ModelAdmin):
    fields = ('employee', 'effective_date', 'employment_status_type','comment')
    list_display = ('employee', 'effective_date', 'employment_status_type','comment')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ('location_name', )
    list_display = ('location_name', )

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    fields = ('division_name', )
    list_display = ('division_name', )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    fields = ('department_name', )
    list_display = ('department_name', )

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = ('job_title_name', )
    list_display = ('job_title_name', )

@admin.register(JobInformation)
class JobInformationAdmin(admin.ModelAdmin):
    fields = ('employee', 'effective_date', 'location',
              'division', 'department', 'job', 'reports_to')
    list_display = ('id', 'employee', 'effective_date', 'location',
              'division', 'department', 'job', 'reports_to')

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    fields = ('currency_name', 'currency_code')
    list_display = ('currency_name', 'currency_code')

@admin.register(ChangeReason)
class ChangeReasonAdmin(admin.ModelAdmin):
    fields = ('change_reason_name', )
    list_display = ('change_reason_name', )

@admin.register(Compensation)
class CompensationAdmin(admin.ModelAdmin):
    fields = (
        'employee',
        'effective_date',
        'pay_type',
        'pay_rate',
        'pay_rate_currency',
        'pay_rate_period',
        'pay_schedule',
        'overtime_status',
        'change_reason',
        'payment_method',
        'comment'
    )
    list_display = (
        'employee',
        'effective_date',
        'pay_type',
        'pay_rate',
        'pay_rate_currency',
        'pay_rate_period',
        'pay_schedule',
        'overtime_status',
        'change_reason',
        'payment_method',
        'comment'
    )

@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    fields = (
        'employee',
        'name',
        'relationship',
        'mobile_phone',
        'home_phone',
        'work_phone',
        'home_email',
        'work_email',
        'address',
        'city',
        'province',
        'nationality',
        'is_primary_contact'
    )
    list_display = (
        'employee',
        'name',
        'relationship',
        'mobile_phone',
        'home_phone',
        'work_phone',
        'home_email',
        'work_email',
        'address',
        'city',
        'province',
        'nationality',
        'is_primary_contact'
    )


@admin.register(Dependant)
class DependantAdmin(admin.ModelAdmin):
    fields = (
        'employee',
        'name',
        'birth_date',
        'national_identification_number',
        'gender',
        'relationship',
        'phone',
        'address',
        'city',
        'province',
        'nationality'
    )
    list_display = (
        'employee',
        'name',
        'birth_date',
        'national_identification_number',
        'gender',
        'relationship',
        'phone',
        'address',
        'city',
        'province',
        'nationality'
    )

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    fields = ('employee', 'note')
    list_display = ('employee', 'note')


@admin.register(Relationship)
class NoteAdmin(admin.ModelAdmin):
    fields = ('relationship_name', )
    list_display = ('relationship_name',)
