import graphene
from graphene_django.types import DjangoObjectType

from fedhr.employee.models import Employee, Country


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        filter_fields = ['first_name', 'last_name']
        interfaces = (graphene.relay.Node,)
        fields = '__all__'


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields = ('id', 'country_name')
