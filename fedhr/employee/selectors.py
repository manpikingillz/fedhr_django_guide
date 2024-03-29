from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from fedhr.common.utils import get_object
from fedhr.employee.models import (
    Employee,
    Note,
    Education,
    VisaInformation)
from fedhr.employee.filters import (
    BaseEmployeeFilter,
    BaseNoteFilter,
    BaseEducationFilter,
    BaseVisaInformationFilter)
from fedhr.employee.models import JobInformation


# Employee =====================================================
def employee_list(*, filters=None) -> QuerySet[Employee]:
    filters = filters or {}

    qs = Employee.objects.filter(removed=False).order_by('id')
    return BaseEmployeeFilter(filters, qs).qs


def employee_detail(*, pk) -> Employee:
    employee = get_object(Employee, pk=pk, removed=False)
    if not employee:
        EMPLOYEE_INSTANCE_NONE = f'Employee with id {pk} not found'
        raise ValidationError(EMPLOYEE_INSTANCE_NONE)
    return employee


# Note =====================================================
def note_list(*, filters=None) -> QuerySet[Note]:
    filters = filters or {}

    qs = Note.objects.filter(removed=False).order_by('-id')
    return BaseNoteFilter(filters, qs).qs


def note_detail(*, pk) -> Note:
    note = get_object(Note, pk=pk, removed=False)
    if not note:
        NOTE_INSTANCE_NONE = f'Note with id {pk} not found'
        raise ValidationError(NOTE_INSTANCE_NONE)
    return note


# Education =====================================================
def education_list(*, filters=None) -> QuerySet[Education]:
    filters = filters or {}

    qs = Education.objects.filter(removed=False).order_by('-end_date')
    return BaseEducationFilter(filters, qs).qs


def education_detail(*, pk) -> Note:
    education = get_object(Education, pk=pk, removed=False)
    if not education:
        EDUCATION_INSTANCE_NONE = f'Education with id {pk} not found'
        raise ValidationError(EDUCATION_INSTANCE_NONE)
    return education

# Visa Information =====================================================
def visa_information_list(*, filters=None) -> QuerySet[VisaInformation]:
    filters = filters or {}

    qs = VisaInformation.objects.filter(removed=False).order_by('-expiration_date')
    return BaseVisaInformationFilter(filters, qs).qs


def visa_information_detail(*, pk) -> Note:
    visa_information = get_object(VisaInformation, pk=pk, removed=False)
    if not visa_information:
        VISA_INFORMATION_INSTANCE_NONE = f'Visa Information with id {pk} not found'
        raise ValidationError(VISA_INFORMATION_INSTANCE_NONE)
    return visa_information

# Job Information =====================================================
def direct_reports_list(*, filters=None) -> QuerySet[Employee]:
    filters = filters or {}
    reports_to_id = filters.get('reports_to_id')

    if not reports_to_id:
        DIRECT_REPORTS_NO_EMPLOYEE_ID_FILTER = f'You must provide reports_to_id (Employee being reported to).'
        raise ValidationError(DIRECT_REPORTS_NO_EMPLOYEE_ID_FILTER)

    direct_reports_ids = JobInformation.objects.filter(reports_to=reports_to_id).values_list('employee_id', flat=True)
    direct_reports = Employee.objects.filter(id__in=direct_reports_ids)
    return direct_reports