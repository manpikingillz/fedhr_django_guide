import graphene

from django.core.exceptions import ValidationError
from rest_framework import serializers

from fedhr.employee.models import Employee
from fedhr.employee.graph.types import EmployeeType
from fedhr.common.utils import get_object


# EMPLOYEE CREATE  ###################################################
class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateInput(graphene.InputObjectType):
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    country = graphene.Int()


class EmployeeCreate(graphene.Mutation):
    employee = graphene.Field(EmployeeType)
    errors = graphene.String()

    class Arguments:
        employee_data = EmployeeCreateInput(required=True)

    def mutate(self, info, employee_data=None, **kwargs):
        serializer = EmployeeCreateSerializer(data=employee_data)
        serializer.is_valid(raise_exception=True)

        created_employee = serializer.save()
        return EmployeeCreate(employee=created_employee)


# EMPLOYEE UPDATE  ##################################################
class EmployeeUpdateSerializer(serializers.ModelSerializer):
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
    employee = graphene.Field(EmployeeType)
    errors = graphene.String()

    class Arguments:
        employee_data = EmployeeUpdateInput(required=True)

    class Meta:
        description = "Updates an employee"

    def mutate(self, info, employee_data=None, **kwargs):
        try:
            instance = get_object(Employee, id=employee_data.get('id'))

            serializer = EmployeeUpdateSerializer(
                instance=instance,
                data=employee_data,
            )
            serializer.is_valid(raise_exception=True)

            updated_instance = serializer.save()
            # TODO: Need to evaluate better approach since we can also do this
            # if we like. in which we wouldn't pass instance to serializer.
            # saved_instance = generic_model_update(
            #     instance=instance,
            #     data=serializer.validated_data)

        except ValidationError as e:
            return EmployeeUpdate(errors=e)
        return EmployeeUpdate(employee=updated_instance)


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
