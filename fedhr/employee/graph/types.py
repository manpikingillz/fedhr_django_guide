import graphene
from graphene_django.types import DjangoObjectType

from fedhr.employee.models import Employee, Country
from fedhr.employee.graph.filters import EmployeeFilter
from fedhr.files.models import File


class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee
        interfaces = (graphene.relay.Node,)
        fields = '__all__'
        # Deciding not to put the filterset_class here because I may use the 
        # EmployeeType ObjectType in places where the filter is not required, e.g in
        # getting an employee details.
        # filterset_class = EmployeeFilter


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields = ('id', 'country_name')


class FileType(DjangoObjectType):
    class Meta:
        model = File
        interfaces = (graphene.relay.Node,)
        fields = '__all__'
