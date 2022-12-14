from django.core.exceptions import ValidationError
import graphene

from rest_framework import serializers

from fedhr.employee.models import Employee
from fedhr.employee.graph.types import EmployeeType
from fedhr.common.utils import get_object
from graphql.error import GraphQLError


# EMPLOYEE CREATE  ###################################################
class EmployeeInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    country_id = graphene.Int()


class EmployeeCreate(graphene.Mutation):
    employee = graphene.Field(EmployeeType)
    errors = graphene.String()

    class Arguments:
        employee_data = EmployeeInput(required=True)

    def mutate(self, info, employee_data=None, **kwargs):
        try:
            employee_for_create = Employee(
                first_name=employee_data.first_name,
                last_name=employee_data.last_name,
                country_id=employee_data.country_id
            )

            employee_for_create.full_clean()
            employee_for_create.save()
        except ValidationError as e:
            return EmployeeCreate(errors=e)

        return EmployeeCreate(employee=employee_for_create)


# EMPLOYEE UPDATE  ##################################################
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeUpdateInput(graphene.InputObjectType):
    id = graphene.ID()
    first_name = graphene.String(
        required=True,
        description="First name of the Employee")
    last_name = graphene.String(required=True)
    country = graphene.Int()
    marital_status = graphene.String(required=False)


class EmployeeUpdate(graphene.Mutation):
    class Arguments:
        employee_data = EmployeeUpdateInput(required=True)

    class Meta:
        description = "Updates an employee"

    employee = graphene.Field(EmployeeType)

    def mutate(self, info, employee_data=None, **kwargs):
        instance = get_object(Employee, id=employee_data.get('id'))

        serializer = EmployeeSerializer(
            instance=instance,
            data=employee_data,
            partial=True)

        serializer.is_valid(raise_exception=True)
        saved_instance = serializer.save()
        return EmployeeUpdate(employee=saved_instance)


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
