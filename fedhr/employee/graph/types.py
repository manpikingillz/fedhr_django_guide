from graphene_django.types import DjangoObjectType

from fedhr.employee.models import Employee


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'  # ('first_name', 'last_name', 'middle_name')
