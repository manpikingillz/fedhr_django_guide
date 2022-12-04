import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from rest_framework.serializers import Serializer, ModelSerializer

from fedhr.employee.models import Employee
from fedhr.employee.graph.types import EmployeeType


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name',)


class EmployeeMutation(SerializerMutation):
    class Meta:
        serializer_class = EmployeeSerializer
        # model_operations = ('create',)
        # only_fields = ('first_name', 'last_name', 'middle_name')
        # lookupfield = 'id'


# class CreateEmployee(graphene.Mutation):
#     class Arguments:
#         first_name = graphene.String(required=True)
#         middle_name = graphene.String(required=False)
#         last_name = graphene.String(required=True)

#     employee = graphene.Field(EmployeeType)

#     @classmethod
#     def mutate(cls, root, info, first_name, middle_name, last_name):
#         employee = Employee(
#             first_name=first_name,
#             middle_name=middle_name,
#             last_name=last_name
#         )
#         employee.save()
#         return CreateEmployee(employee=employee)


# class UpdateEmployee(graphene.Mutation):
#     class Arguments:
#         first_name = graphene.String(required=True)
#         last_name = graphene.String(required=True)

#     employee = graphene.Field(EmployeeType)

#     @classmethod
#     def mutate(cls, root, info, first_name, last_name):
#         employee = Employee.objects.get(first_name=first_name)
#         employee.last_name = last_name
#         employee.save()
#         return UpdateEmployee(employee=employee)


class DeleteEmployee(graphene.Mutation):
    class Arguments:
        # first_name = graphene.String(required=True)
        id = graphene.ID()

    employee = graphene.Field(EmployeeType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        employee = Employee.objects.get(id=kwargs.get('id'))
        employee.delete()
        return cls(employee=employee)


class EmployeeMutations(graphene.ObjectType):
    # create_employee = CreateEmployee.Field()
    # update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()
    employee_mutation = EmployeeMutation.Field()
