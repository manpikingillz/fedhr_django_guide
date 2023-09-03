from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from fedhr.common.utils import get_object
from fedhr.employee.models import Employee
from fedhr.employee.filters import BaseEmployeeFilter
from fedhr.employee.models import Note, Education
from fedhr.employee.filters import BaseNoteFilter, BaseEducationFilter


# Employee
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


# Note
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

# Education
def education_list(*, filters=None) -> QuerySet[Education]:
    filters = filters or {}

    qs = Education.objects.filter(removed=False).order_by('-id')
    return BaseEducationFilter(filters, qs).qs


def education_detail(*, pk) -> Note:
    education = get_object(Education, pk=pk, removed=False)
    if not education:
        EDUCATION_INSTANCE_NONE = f'Education with id {pk} not found'
        raise ValidationError(EDUCATION_INSTANCE_NONE)
    return education