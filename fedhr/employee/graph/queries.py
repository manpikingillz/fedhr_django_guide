import graphene

from fedhr.employee.models import Employee
from fedhr.employee.graph.types import EmployeeType


class EmployeeQueries(graphene.ObjectType):
    employees = graphene.List(
        EmployeeType,
        limit=graphene.Int(),
        offset=graphene.Int())
    employee_by_first_name = graphene.Field(
        EmployeeType, first_name=graphene.String())

    # Resolvers
    def resolve_employees(self, info, limit=None, offset=None,):
        queryset = Employee.objects.all().order_by('-id')

        if limit and offset:
            end = offset + limit
            queryset = queryset[offset:end]

        return queryset

    def resolve_employee_by_first_name(self, info, first_name):
        try:
            return Employee.objects.get(first_name=first_name)
        except Employee.DoesNotExist:
            return None
