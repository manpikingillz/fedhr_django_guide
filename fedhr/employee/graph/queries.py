import graphene

from graphene_django.filter import DjangoFilterConnectionField

from fedhr.employee.models import Employee
from fedhr.employee.graph.types import EmployeeType
from fedhr.employee.graph.filters import EmployeeFilter


class EmployeeQueries(graphene.ObjectType):

    employees = DjangoFilterConnectionField(
        EmployeeType, filterset_class=EmployeeFilter)
    employee_detail = graphene.relay.Node.Field(
        EmployeeType)

    def resolve_employees(self, info, **kwargs):
        filters = kwargs or {}
        queryset = Employee.objects.all()
        # We could just pass kwargs only and we're still good.
        return EmployeeFilter(filters, queryset=queryset).qs
