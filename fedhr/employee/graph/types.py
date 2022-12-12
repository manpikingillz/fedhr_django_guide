from graphene_django.types import DjangoObjectType

from fedhr.employee.models import Employee, Country


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        fields = '__all__'


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields = ('id', 'country_name')
