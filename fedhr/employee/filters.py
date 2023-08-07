import django_filters

from fedhr.employee.models import Employee
from fedhr.employee.models import Note

class BaseEmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email')


class BaseNoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = ('note', 'employee')
