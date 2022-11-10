import django_filters

from fedhr.employee.models import Employee

class BaseEmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email')
