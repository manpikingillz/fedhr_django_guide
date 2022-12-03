import graphene

from fedhr.employee.models import Employee
from fedhr.employee.graph.types import EmployeeType


class EmployeeQueries(graphene.ObjectType):
    employees = graphene.List(EmployeeType)
    employee_by_first_name = graphene.Field(
        EmployeeType, first_name=graphene.String())

    # Resolvers
    def resolve_employees(self, info):
        return Employee.objects.all()

    def resolve_employee_by_first_name(self, info, first_name):
        try:
            return Employee.objects.get(first_name=first_name)
        except Employee.DoesNotExist:
            return None
