from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status
from fedhr.api.mixins import ApiAuthMixin
from fedhr.common.utils import get_object
from fedhr.employee.services import employee_create, employee_update, employee_delete
from fedhr.employee.selectors import employee_detail, employee_list
from fedhr.employee.models import Employee


class EmployeeCreateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=255, required=True)
        last_name = serializers.CharField(max_length=255, required=True)
        middle_name = serializers.CharField(max_length=255, required=False)
        gender = serializers.ChoiceField(choices=Employee.Gender.choices, required=True)
        email = serializers.EmailField(max_length=255, required=True)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee_create(**serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class EmployeeListApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=255, required=True)
        last_name = serializers.CharField(max_length=255, required=True)
        middle_name = serializers.CharField(max_length=255, required=False)
        full_name = serializers.CharField()
        gender =  serializers.ChoiceField(choices=Employee.Gender.choices, required=True)
        email = serializers.EmailField(max_length=255, required=True)


    class FilterSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=255, required=False)
        last_name = serializers.CharField(max_length=255, required=False)
        email = serializers.EmailField(max_length=255, required=False)

    def get(self, request):
        # Make sure the filters are valid
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        employees = employee_list(filters=filters_serializer.validated_data)

        data = self.OutputSerializer(employees, many=True).data
        return Response(data)


class EmployeeDetailApi(ApiAuthMixin, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        first_name = serializers.CharField(max_length=255, required=True)
        last_name = serializers.CharField(max_length=255, required=True)
        middle_name = serializers.CharField(max_length=255, required=False)
        full_name = serializers.CharField()
        gender =  serializers.ChoiceField(choices=Employee.Gender.choices, required=True)
        email = serializers.EmailField(max_length=255, required=True)

    def get(self, request, employee_id):

        employee = employee_detail(pk=employee_id)

        data = self.OutputSerializer(employee).data
        return Response(data)


class EmployeeUpdateApi(ApiAuthMixin, APIView):
    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField(max_length=255, required=False)
        last_name = serializers.CharField(max_length=255, required=False)
        middle_name = serializers.CharField(max_length=255, required=False)
        gender =  serializers.ChoiceField(choices=Employee.Gender.choices, required=False)
        email = serializers.EmailField(max_length=255, required=False)

    def post(self, request, employee_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employee = get_object(Employee, pk=employee_id)

        employee_update(employee=employee, data=serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class EmployeeDeleteApi(ApiAuthMixin, APIView):
    def post(self, request, employee_id):
        employee = get_object(Employee, pk=employee_id)

        employee_delete(employee=employee)

        return Response(status=status.HTTP_200_OK)
