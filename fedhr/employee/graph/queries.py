import graphene

from fedhr.employee.models import Employee
from fedhr.employee.graph.types import EmployeeType

from graphene_django.filter import DjangoFilterConnectionField


class EmployeeQueries(graphene.ObjectType):

    employees = DjangoFilterConnectionField(
        EmployeeType)
    employee_detail = graphene.relay.Node.Field(
        EmployeeType)

    def resolve_employees(self, info, **kwargs):
        return Employee.objects.all().order_by('-id')
