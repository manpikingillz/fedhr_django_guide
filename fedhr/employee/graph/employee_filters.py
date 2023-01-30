from django_filters import FilterSet, OrderingFilter

from fedhr.employee.models import Employee


class EmployeeFilter(FilterSet):
    class Meta:
        model = Employee
        fields = {
            'first_name': ('exact', 'contains'),
            'last_name': ('exact', 'contains'),
        }
    order_by = OrderingFilter(
        fields=('id', 'first_name', 'last_name'),
    )
