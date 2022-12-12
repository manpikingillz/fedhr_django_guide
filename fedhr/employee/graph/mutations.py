import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from rest_framework import serializers

from fedhr.employee.models import Employee, Country
from fedhr.employee.graph.types import EmployeeType


# EMPLOYEE CREATE  ###################################################
class EmployeeInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    country_id = graphene.Int()


class EmployeeCreate(graphene.Mutation):
    class Arguments:
        employee_data = EmployeeInput(required=True)

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, employee_data=None, **kwargs):
        created_employee = Employee.objects.create(
            first_name=employee_data.first_name,
            last_name=employee_data.last_name,
            country_id=employee_data.country_id
        )

        return EmployeeCreate(employee=created_employee)


# EMPLOYEE UPDATE  ##################################################
class EmployeeSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(required=False)
    marital_status = serializers.CharField(required=False)
    country = serializers.RelatedField(required=False, queryset=Country.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeUpdate(SerializerMutation):
    class Meta:
        serializer_class = EmployeeSerializer
        model_operations = ('update', )
        lookup_field = 'id'


# EMPLOYEE DELETE  ###################################################
class EmployeeDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(root, info, **kwargs):
        employee = Employee.objects.get(id=kwargs.get('id'))
        try:
            employee.delete()
            # message = 'Deleted Successafully'
        except Exception:
            pass

        return EmployeeDelete(employee=employee)


class EmployeeMutations(graphene.ObjectType):
    employee_delete = EmployeeDelete.Field()
    employee_update = EmployeeUpdate.Field()
    employeeCreate = EmployeeCreate.Field()
