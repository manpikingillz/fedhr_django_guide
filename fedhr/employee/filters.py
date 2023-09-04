import django_filters

from fedhr.employee.models import Employee
from fedhr.employee.models import (
    Note, Education, VisaInformation)


class BaseEmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email')


class BaseNoteFilter(django_filters.FilterSet):
    note = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Note
        fields = ('note', 'employee')


class BaseEducationFilter(django_filters.FilterSet):
    note = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Education
        fields = ('institution_name', 'employee')


class BaseVisaInformationFilter(django_filters.FilterSet):

    class Meta:
        model = VisaInformation
        fields = ('employee',)