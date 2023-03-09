from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from fedhr.common.utils import get_object
from fedhr.employee.models import Employee
from fedhr.employee.filters import BaseEmployeeFilter


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
